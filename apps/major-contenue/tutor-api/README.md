# Major Tutor API

API de tutorat intelligent pour les élèves mauritaniens de CM2, propulsée par **Mistral 7B** (via Ollama) + **Whisper** (STT) + **Edge-TTS**.

## Prérequis

- **Python 3.11+**
- **Ollama** installé et lancé — https://ollama.com
- **ffmpeg** installé (requis par faster-whisper)

## Installation rapide

```bash
# 1. Installer Ollama et télécharger Mistral
ollama pull mistral

# 2. Créer un environnement virtuel
cd tutor-api
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Linux/Mac

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Lancer l'API
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

L'API est accessible sur http://localhost:8000

Documentation Swagger : http://localhost:8000/docs

## Endpoints

| Méthode | Endpoint | Description |
|---------|----------|-------------|
| `POST` | `/api/v1/chat/` | Chat texte avec le tuteur |
| `POST` | `/api/v1/chat/stream` | Chat avec streaming SSE |
| `POST` | `/api/v1/voice/tts` | Texte → Audio (base64 MP3) |
| `POST` | `/api/v1/voice/tts/audio` | Texte → Audio brut (MP3) |
| `POST` | `/api/v1/voice/stt` | Audio → Texte (Whisper) |
| `POST` | `/api/v1/voice/chat` | Pipeline complet : Audio → STT → LLM → TTS |
| `GET` | `/api/v1/voice/voices` | Lister les voix TTS disponibles |
| `GET` | `/health` | Vérifier l'état de l'API |

## Exemples d'utilisation

### Chat texte (arabe)

```bash
curl -X POST http://localhost:8000/api/v1/chat/ \
  -H "Content-Type: application/json" \
  -d '{
    "message": "ما هي عاصمة موريتانيا؟",
    "lang": "ar",
    "subject": "history_geo"
  }'
```

### Chat texte (français)

```bash
curl -X POST http://localhost:8000/api/v1/chat/ \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Comment on calcule le périmètre d'un rectangle ?",
    "lang": "fr",
    "subject": "math"
  }'
```

### Chat streaming

```bash
curl -N -X POST http://localhost:8000/api/v1/chat/stream \
  -H "Content-Type: application/json" \
  -d '{"message": "اشرح لي الكسور", "lang": "ar", "subject": "math"}'
```

### Text-to-Speech

```bash
curl -X POST http://localhost:8000/api/v1/voice/tts/audio \
  -H "Content-Type: application/json" \
  -d '{"text": "أحسنت يا بطل! إجابة ممتازة", "lang": "ar"}' \
  --output response.mp3
```

### Speech-to-Text

```bash
curl -X POST http://localhost:8000/api/v1/voice/stt \
  -F "audio=@question.wav" \
  -F "language=ar"
```

### Pipeline vocal complet

```bash
curl -X POST http://localhost:8000/api/v1/voice/chat \
  -F "audio=@question.wav" \
  -F "lang=ar" \
  -F "subject=math"
```

## Configuration (.env)

| Variable | Défaut | Description |
|----------|--------|-------------|
| `TUTOR_OLLAMA_BASE_URL` | `http://localhost:11434` | URL d'Ollama |
| `TUTOR_OLLAMA_MODEL` | `mistral` | Modèle LLM |
| `TUTOR_DEFAULT_LANG` | `ar` | Langue par défaut |
| `TUTOR_WHISPER_MODEL_SIZE` | `base` | Taille du modèle Whisper (tiny/base/small/medium) |
| `TUTOR_WHISPER_DEVICE` | `cpu` | Device Whisper (cpu/cuda) |
| `TUTOR_TTS_VOICE_AR` | `ar-SA-HamedNeural` | Voix TTS arabe |
| `TUTOR_TTS_VOICE_FR` | `fr-FR-HenriNeural` | Voix TTS française |

## Architecture

```
tutor-api/
├── main.py              # Point d'entrée FastAPI
├── config.py            # Configuration (pydantic-settings)
├── requirements.txt     # Dépendances Python
├── .env                 # Variables d'environnement
├── models/
│   └── schemas.py       # Modèles Pydantic (request/response)
├── prompts/
│   └── tutor.py         # Prompts système (arabe + français)
├── routers/
│   ├── chat.py          # Routes chat (texte + streaming)
│   └── voice.py         # Routes voix (TTS, STT, pipeline)
└── services/
    ├── llm.py           # Client Ollama (Mistral)
    ├── tts.py           # Text-to-Speech (edge-tts)
    └── stt.py           # Speech-to-Text (faster-whisper)
```
