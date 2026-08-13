import base64
import hashlib
import io
import json
import os
import time
from collections import OrderedDict

import edge_tts
import httpx
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI
from pydantic import BaseModel

try:
    from redis import Redis

    REDIS_AVAILABLE = True
except ImportError:
    REDIS_AVAILABLE = False

load_dotenv()


def parse_allowed_origins() -> list[str]:
    raw = os.getenv("ALLOWED_ORIGINS", "*").strip()
    if not raw or raw == "*":
        return ["*"]
    return [origin.strip() for origin in raw.split(",") if origin.strip()]


app = FastAPI(title="Major API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=parse_allowed_origins(),
    allow_origin_regex=r"https://major-eval(?:-[a-z0-9-]+)?\.vercel\.app",
    allow_methods=["POST", "GET", "OPTIONS"],
    allow_headers=["*"],
)

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY", "").strip(),
    http_client=httpx.Client(),
)

RATE_LIMIT_PER_HOUR = int(os.getenv("RATE_LIMIT_PER_HOUR", "30"))

# TTS (edge-tts - voix neurales gratuites, sans cle API)
TTS_VOICE_AR = os.getenv("TTS_VOICE_AR", "ar-SA-HamedNeural")
TTS_VOICE_FR = os.getenv("TTS_VOICE_FR", "fr-FR-HenriNeural")
TTS_RATE_LIMIT_PER_HOUR = int(os.getenv("TTS_RATE_LIMIT_PER_HOUR", "180"))
TTS_MAX_CHARS = 500
TTS_MEMORY_CACHE_ITEMS = int(os.getenv("TTS_MEMORY_CACHE_ITEMS", "64"))
tts_memory_cache: OrderedDict[str, tuple[float, str]] = OrderedDict()

redis: Redis | None = None
if REDIS_AVAILABLE:
    try:
        redis = Redis.from_url(
            os.getenv("REDIS_URL", "redis://localhost:6379"),
            decode_responses=True,
            socket_connect_timeout=2,
        )
        redis.ping()
        print("Redis connected")
    except Exception as exc:
        print(f"Redis unavailable ({exc}) - cache disabled")
        redis = None


VALIDATE_PROMPT = """Analyse cette photo de cahier scolaire. Reponds UNIQUEMENT en JSON valide, sans markdown :
{
  "hasFrame": true,
  "hasAnswer": true,
  "isExercise": true,
  "isMajor": true,
  "failReason": ""
}

DEFINITIONS IMPORTANTES avant de repondre :
- TEXTE IMPRIME = texte de la consigne, enonces, instructions, lignes vides imprimees => ce n'est PAS une reponse
- ECRITURE MANUSCRITE = traces au stylo ou crayon AJOUTEES par l'eleve dans les zones de reponse => c'est une reponse

Regles :

- "hasFrame": true si cadre imprime rectangulaire visible autour d'un exercice.

- "hasAnswer": CRITIQUE. Cherche des traces de stylo/crayon ajoutees PAR L'ELEVE.
  * false si les zones de reponse sont VIDES (lignes blanches, blancs non remplis)
  * false si tu ne vois que du texte imprime, meme si c'est un enonce long
  * false si tu vois seulement les tirets "..." ou "_____" non remplis
  * true UNIQUEMENT si des mots, chiffres ou dessins ont ete ecrits a la main dans les espaces prevus
  * EN CAS DE DOUTE : false

- "isExercise": true si page de cahier scolaire ou feuille d'exercice.

- "isMajor": true si logo 4 carres bleus 2x2 visible, ou 2+ indices parmi : fond creme, badge colore, en-tete "Major 6AF".

- "failReason": si hasFrame/hasAnswer/isExercise est false, explique en 1 phrase. Sinon vide."""

ANALYZE_CORRECTION_PROMPT = """Analyse cette photo de copie avant correction.
Reponds UNIQUEMENT en JSON valide, sans markdown, avec exactement ce format :
{
  "hasHandwriting": true,
  "quality": "good",
  "exerciseFormat": "single",
  "answeredCount": 3,
  "emptyCount": 1,
  "requiresReview": false,
  "reason": ""
}

Regles :
- "hasHandwriting": true seulement si tu vois une vraie reponse manuscrite.
- "quality": vaut obligatoirement "poor", "fair" ou "good".
- "exerciseFormat": vaut obligatoirement "single", "multi" ou "unknown".
- "answeredCount": nombre estime de zones avec reponse manuscrite lisible.
- "emptyCount": nombre estime de zones manifestement laissees vides.
- "requiresReview": true si la photo est floue, coupee, trop sombre, inclinee, ou ambiguë.
- "reason": phrase courte expliquant le principal risque si requiresReview=true, sinon chaine vide.
- En cas de doute, sois prudent et baisse la qualite ou active requiresReview.
"""

SYSTEM_PROMPT = """Tu es Major, un professeur bienveillant pour les eleves mauritaniens de 6AF.
Tu corriges des copies manuscrites avec precision, justice et douceur.
Tu parles simplement pour qu'un eleve et son parent comprennent tout de suite.

DISTINCTION FONDAMENTALE :
- Texte IMPRIME (consigne, enonce, instructions) = ce que le cahier a imprime. Tu l'ignores pour la note.
- Ecriture MANUSCRITE (au stylo/crayon par l'eleve) = la seule chose que tu corriges.

REGLES DE NOTATION (CRITIQUES) :
1. Avant tout : cherche de l'ecriture manuscrite dans les zones de reponse.
2. Si tu ne vois QUE du texte imprime et des espaces vides => score = 0, whyThisScore = "Aucune reponse manuscrite detectee. L'exercice semble non complete.", confidence = "low". Ne dis pas que c'est correct.
3. Sur les items avec reponse manuscrite : compte corrects vs incorrects.
4. Le score = round((items_corrects / items_repondus) * 10).
5. Une case vide = non evalue, pas faux. Ne penalise pas les espaces vides.
6. Si l'ecriture est difficile a lire, donne le benefice du doute.
- Garde un ton encourageant meme en cas de difficulte
- Reponds UNIQUEMENT en JSON valide avec exactement ce format :
{
  "score": 7,
  "scoreLabel": "7 / 10",
  "isCorrect": true,
  "mastery": "fragile",
  "confidence": "medium",
  "whyThisScore": "Explication courte et honnete de la note",
  "rubric": { "understanding": 3, "accuracy": 2, "method": 3, "presentation": 4 },
  "pointsForts": ["..."],
  "corrections": ["..."],
  "focusAreas": ["grammar", "spelling"],
  "encouragement": "Message motivant court et personnel",
  "conseil": "Un seul conseil pratique pour progresser"
}"""


def cache_get(key: str):
    if not redis:
        return None
    try:
        raw = redis.get(key)
        return json.loads(raw) if raw else None
    except Exception:
        return None


def cache_set(key: str, value: dict, ttl: int):
    if not redis:
        return
    try:
        redis.setex(key, ttl, json.dumps(value, ensure_ascii=False))
    except Exception:
        pass


def image_key(prefix: str, image_base64: str, **extras) -> str:
    content = image_base64 + json.dumps(extras, sort_keys=True)
    digest = hashlib.sha256(content.encode()).hexdigest()
    return f"major:{prefix}:{digest}"


def check_rate_limit(request: Request) -> bool:
    if not redis:
        return True
    ip = request.client.host if request.client else "unknown"
    key = f"major:rl:{ip}"
    try:
        count = redis.incr(key)
        if count == 1:
            redis.expire(key, 3600)
        return count <= RATE_LIMIT_PER_HOUR
    except Exception:
        return True


def check_tts_rate_limit(request: Request) -> bool:
    if not redis:
        return True
    ip = request.client.host if request.client else "unknown"
    key = f"major:rl:tts:{ip}"
    try:
        count = redis.incr(key)
        if count == 1:
            redis.expire(key, 3600)
        return count <= TTS_RATE_LIMIT_PER_HOUR
    except Exception:
        return True


def tts_cache_get(key: str):
    if redis:
        try:
            cached = redis.get(key)
            if cached:
                return cached
        except Exception:
            pass

    memory_entry = tts_memory_cache.get(key)
    if not memory_entry:
        return None
    expires_at, value = memory_entry
    if expires_at <= time.time():
        tts_memory_cache.pop(key, None)
        return None
    tts_memory_cache.move_to_end(key)
    return value


def tts_cache_set(key: str, value: str, ttl: int):
    tts_memory_cache[key] = (time.time() + ttl, value)
    tts_memory_cache.move_to_end(key)
    while len(tts_memory_cache) > TTS_MEMORY_CACHE_ITEMS:
        tts_memory_cache.popitem(last=False)

    if redis:
        try:
            redis.setex(key, ttl, value)
        except Exception:
            pass


def clamp(value, lo, hi):
    return max(lo, min(hi, value))


def safe_array(value):
    return value if isinstance(value, list) else []


def safe_object(value):
    return value if isinstance(value, dict) else {}


def safe_int(value, default=0):
    return int(value) if isinstance(value, (int, float)) else default


def parse_json_response(raw: str, fallback: dict) -> dict:
    try:
        parsed = json.loads(raw)
        return parsed if isinstance(parsed, dict) else fallback
    except json.JSONDecodeError:
        start, end = raw.find("{"), raw.rfind("}")
        if start >= 0 and end > start:
            try:
                parsed = json.loads(raw[start : end + 1])
                return parsed if isinstance(parsed, dict) else fallback
            except json.JSONDecodeError:
                return fallback
        return fallback


def call_vision_json(
    *,
    model: str,
    max_tokens: int,
    system_prompt: str,
    user_text: str,
    image_base64: str,
    mime_type: str,
    detail: str,
    fallback: dict,
) -> dict:
    response = client.chat.completions.create(
        model=model,
        max_tokens=max_tokens,
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": system_prompt},
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": user_text},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:{mime_type};base64,{image_base64}",
                            "detail": detail,
                        },
                    },
                ],
            },
        ],
    )
    raw = response.choices[0].message.content or "{}"
    return parse_json_response(raw, fallback)


def build_analysis_result(parsed: dict) -> dict:
    quality = parsed.get("quality") if parsed.get("quality") in ("poor", "fair", "good") else "fair"
    exercise_format = (
        parsed.get("exerciseFormat")
        if parsed.get("exerciseFormat") in ("single", "multi", "unknown")
        else "unknown"
    )
    return {
        "hasHandwriting": bool(parsed.get("hasHandwriting")),
        "quality": quality,
        "exerciseFormat": exercise_format,
        "answeredCount": int(clamp(safe_int(parsed.get("answeredCount")), 0, 20)),
        "emptyCount": int(clamp(safe_int(parsed.get("emptyCount")), 0, 20)),
        "requiresReview": bool(parsed.get("requiresReview")),
        "reason": str(parsed.get("reason") or ""),
    }


def analyze_submission(image_base64: str, mime_type: str) -> dict:
    parsed = call_vision_json(
        model="gpt-4o",
        max_tokens=220,
        system_prompt=ANALYZE_CORRECTION_PROMPT,
        user_text="Observe cette photo et fais une analyse preparatoire avant correction.",
        image_base64=image_base64,
        mime_type=mime_type,
        detail="high",
        fallback={
            "hasHandwriting": False,
            "quality": "fair",
            "exerciseFormat": "unknown",
            "answeredCount": 0,
            "emptyCount": 0,
            "requiresReview": True,
            "reason": "Analyse preparatoire indisponible.",
        },
    )
    return build_analysis_result(parsed)


class ValidateScanRequest(BaseModel):
    imageBase64: str
    mimeType: str = "image/jpeg"
    model: str = "gpt-4o"


class TTSRequest(BaseModel):
    text: str
    lang: str = "ar"


class CorrectExerciseRequest(BaseModel):
    imageBase64: str
    mimeType: str = "image/jpeg"
    title: str = ""
    subject: str = ""
    subjectId: str = ""
    summary: str = ""
    rule: str = ""
    topicPrompt: str = ""
    isArabic: bool = False


@app.get("/health")
def health():
    return {
        "status": "ok",
        "redis": redis is not None and redis.ping(),
        "origins": parse_allowed_origins(),
    }


@app.post("/tts")
async def text_to_speech(req: TTSRequest, request: Request):
    text = req.text.strip()
    if not text:
        raise HTTPException(status_code=400, detail="Texte vide.")
    if len(text) > TTS_MAX_CHARS:
        raise HTTPException(status_code=400, detail=f"Texte trop long (max {TTS_MAX_CHARS} caracteres).")

    if not check_tts_rate_limit(request):
        raise HTTPException(status_code=429, detail="Limite de synthese vocale atteinte. Reessayez plus tard.")

    voice = TTS_VOICE_AR if req.lang == "ar" else TTS_VOICE_FR
    cache_key = "major:tts:" + hashlib.sha256(f"{voice}:{text}".encode()).hexdigest()

    cached = tts_cache_get(cache_key)
    if cached:
        return {"audioBase64": cached, "lang": req.lang, "_cached": True}

    try:
        communicate = edge_tts.Communicate(text, voice)
        audio_buffer = io.BytesIO()
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio_buffer.write(chunk["data"])
        audio_bytes = audio_buffer.getvalue()
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"{type(exc).__name__}: {exc}")

    if not audio_bytes:
        raise HTTPException(status_code=500, detail="Synthese vocale vide.")

    audio_base64 = base64.b64encode(audio_bytes).decode("utf-8")
    tts_cache_set(cache_key, audio_base64, ttl=30 * 24 * 3600)
    return {"audioBase64": audio_base64, "lang": req.lang}


@app.post("/validate-scan")
def validate_scan(req: ValidateScanRequest):
    key = image_key("validate", req.imageBase64, model=req.model)
    cached = cache_get(key)
    if cached:
        return {**cached, "_cached": True}

    try:
        result = call_vision_json(
            model=req.model,
            max_tokens=120,
            system_prompt=VALIDATE_PROMPT,
            user_text="Analyse cette photo et reponds en JSON.",
            image_base64=req.imageBase64,
            mime_type=req.mimeType,
            detail="low",
            fallback={
                "hasFrame": False,
                "hasAnswer": False,
                "isExercise": False,
                "isMajor": False,
                "failReason": "Reponse invalide du serveur.",
            },
        )
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"{type(exc).__name__}: {exc}")

    cache_set(key, result, ttl=1800)
    return result


@app.post("/correct-exercise")
def correct_exercise(req: CorrectExerciseRequest, request: Request):
    if not check_rate_limit(request):
        raise HTTPException(
            status_code=429,
            detail="Limite de corrections atteinte. Reessayez dans une heure.",
        )

    key = image_key("correct", req.imageBase64, subjectId=req.subjectId, title=req.title)
    cached = cache_get(key)
    if cached:
        return {**cached, "_cached": True}

    try:
        analysis = analyze_submission(req.imageBase64, req.mimeType)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"{type(exc).__name__}: {exc}")

    if not analysis["hasHandwriting"]:
        result = {
            "score": 0,
            "scoreLabel": "0 / 10",
            "isCorrect": False,
            "mastery": "fragile",
            "confidence": "low",
            "whyThisScore": "Aucune reponse manuscrite lisible n'a ete detectee sur la copie.",
            "rubric": {
                "understanding": 0,
                "accuracy": 0,
                "method": 0,
                "presentation": 0,
            },
            "pointsForts": [],
            "corrections": [],
            "focusAreas": [],
            "encouragement": "Prends une photo nette apres avoir rempli l'exercice, puis essaie encore.",
            "conseil": "Ecris la reponse dans les zones prevues avant de reprendre la photo.",
            "_analysis": analysis,
        }
        cache_set(key, result, ttl=3600)
        return result

    lang_note = (
        "La matiere est en ARABE. Les retours doivent etre en arabe clair et naturel."
        if req.isArabic
        else "La matiere est en FRANCAIS. Reponds en francais."
    )
    user_text = "\n".join(
        filter(
            bool,
            [
                f"Matiere : {req.subject}",
                f"Identifiant matiere : {req.subjectId}",
                f"Chapitre : {req.title}",
                f"Contexte du cours : {req.summary}" if req.summary else "",
                f"Regle cle : {req.rule}" if req.rule else "",
                f"Choisis les focusAreas uniquement parmi ces ids : {req.topicPrompt}"
                if req.topicPrompt
                else "",
                (
                    "Analyse preparatoire : "
                    f"quality={analysis['quality']}, "
                    f"format={analysis['exerciseFormat']}, "
                    f"answeredCount={analysis['answeredCount']}, "
                    f"emptyCount={analysis['emptyCount']}."
                ),
                f"Risque photo : {analysis['reason']}"
                if analysis["requiresReview"] and analysis["reason"]
                else "",
                lang_note,
                "",
                (
                    "Voici la photo de la copie de l'eleve. "
                    "Corrige-la, donne une note honnete, explique pourquoi "
                    "et propose 1 a 3 focusAreas pour l'entrainement suivant."
                ),
            ],
        )
    )

    try:
        parsed = call_vision_json(
            model="gpt-4o",
            max_tokens=900,
            system_prompt=SYSTEM_PROMPT,
            user_text=user_text,
            image_base64=req.imageBase64,
            mime_type=req.mimeType,
            detail="high",
            fallback={},
        )
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"{type(exc).__name__}: {exc}")

    raw_score = parsed.get("score", 0)
    score = int(clamp(raw_score if isinstance(raw_score, (int, float)) else 0, 0, 10))
    if analysis["requiresReview"] and score > 8:
        score = 8
    if analysis["answeredCount"] == 0:
        score = 0

    default_rubric = int(clamp(round(score / 2), 0, 5))
    rubric = safe_object(parsed.get("rubric"))
    points_forts = [str(item) for item in safe_array(parsed.get("pointsForts")) if item][:4]
    corrections = [str(item) for item in safe_array(parsed.get("corrections")) if item][:4]
    focus_areas = [str(item) for item in safe_array(parsed.get("focusAreas")) if item][:3]

    confidence = parsed.get("confidence") if parsed.get("confidence") in ("low", "medium", "high") else "medium"
    if analysis["quality"] == "poor":
        confidence = "low"
    elif analysis["quality"] == "fair" and confidence == "high":
        confidence = "medium"

    why_this_score = str(parsed.get("whyThisScore") or "")
    if score == 0 and analysis["answeredCount"] == 0:
        why_this_score = "Aucune reponse manuscrite exploitable n'a ete detectee sur la photo."
    elif analysis["requiresReview"] and not why_this_score:
        why_this_score = analysis["reason"] or "La photo demande une verification supplementaire."

    result = {
        "score": score,
        "scoreLabel": f"{score} / 10",
        "isCorrect": bool(parsed.get("isCorrect", score >= 5)),
        "mastery": (
            parsed.get("mastery")
            if parsed.get("mastery") in ("fragile", "correct", "solide")
            else ("solide" if score >= 8 else "correct" if score >= 5 else "fragile")
        ),
        "confidence": confidence,
        "whyThisScore": why_this_score,
        "rubric": {
            "understanding": int(clamp(rubric.get("understanding", default_rubric), 0, 5)),
            "accuracy": int(clamp(rubric.get("accuracy", default_rubric), 0, 5)),
            "method": int(clamp(rubric.get("method", default_rubric), 0, 5)),
            "presentation": int(clamp(rubric.get("presentation", 3), 0, 5)),
        },
        "pointsForts": points_forts,
        "corrections": corrections,
        "focusAreas": focus_areas,
        "encouragement": str(parsed.get("encouragement") or ""),
        "conseil": str(parsed.get("conseil") or ""),
        "_analysis": analysis,
    }

    cache_set(key, result, ttl=86400)
    return result
