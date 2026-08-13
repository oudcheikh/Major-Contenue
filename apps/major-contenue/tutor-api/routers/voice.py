import json

from fastapi import APIRouter, HTTPException, UploadFile, File, Form
from fastapi.responses import StreamingResponse

from models import TTSRequest, TTSResponse, VoiceChatResponse
from services.llm import ollama_client
from services.tts import tts_service
from services.stt import stt_service
from config import settings

router = APIRouter(prefix="/voice", tags=["Voice"])


@router.post("/tts", response_model=TTSResponse)
async def text_to_speech(request: TTSRequest):
    """Convert text to speech audio (MP3, base64-encoded)."""
    try:
        audio_b64 = await tts_service.synthesize_base64(request.text, request.lang)
        return TTSResponse(audio_base64=audio_b64, lang=request.lang)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"TTS error: {e}")


@router.post("/tts/audio")
async def text_to_speech_raw(request: TTSRequest):
    """Convert text to speech and return raw MP3 audio."""
    try:
        audio_bytes = await tts_service.synthesize(request.text, request.lang)
        return StreamingResponse(
            iter([audio_bytes]),
            media_type="audio/mpeg",
            headers={"Content-Disposition": "inline; filename=tutor_response.mp3"},
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"TTS error: {e}")


@router.post("/stt")
async def speech_to_text(
    audio: UploadFile = File(...),
    language: str = Form(default=None),
):
    """Transcribe audio file to text using Whisper."""
    audio_bytes = await audio.read()
    if len(audio_bytes) == 0:
        raise HTTPException(status_code=400, detail="Empty audio file")
    try:
        result = await stt_service.transcribe(audio_bytes, language=language)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"STT error: {e}")


@router.post("/chat", response_model=VoiceChatResponse)
async def voice_chat(
    audio: UploadFile = File(...),
    lang: str = Form(default="fr"),
    lesson_id: str = Form(default=None),
    student_name: str = Form(default="Eleve"),
    conversation_history: str = Form(default="[]"),
):
    """Full voice pipeline: STT -> LLM -> TTS."""
    audio_bytes = await audio.read()
    if len(audio_bytes) == 0:
        raise HTTPException(status_code=400, detail="Empty audio file")

    # 1. STT
    try:
        stt_result = await stt_service.transcribe(audio_bytes, language=lang)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"STT error: {e}")

    transcript = stt_result["text"]
    if not transcript.strip():
        raise HTTPException(status_code=400, detail="No speech detected")

    # 2. Build context from lesson if provided
    lesson_context = None
    if lesson_id:
        from services.knowledge import build_lesson_context
        lesson_context = build_lesson_context(lesson_id)

    # 3. LLM
    try:
        llm_result = await ollama_client.chat(
            user_message=transcript,
            lang=lang,
            lesson_context=lesson_context,
        )
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"LLM error: {e}")

    reply_text = llm_result["reply"]

    # 4. TTS
    try:
        reply_audio_b64 = await tts_service.synthesize_base64(reply_text, lang)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"TTS error: {e}")

    return VoiceChatResponse(
        transcript=transcript,
        reply_text=reply_text,
        reply_audio_base64=reply_audio_b64,
        model=llm_result["model"],
    )


@router.get("/voices")
async def list_voices(lang_prefix: str = "ar"):
    """List available TTS voices."""
    voices = await tts_service.list_voices(lang_prefix)
    return {"voices": voices, "count": len(voices)}
