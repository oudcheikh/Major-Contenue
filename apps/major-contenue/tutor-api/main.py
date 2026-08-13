import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import settings
from models import HealthResponse
from routers import chat_router, voice_router, mentor_router, courses_router, studio_router
from services.llm import ollama_client
from services.knowledge import list_all_lesson_ids


@asynccontextmanager
async def lifespan(app: FastAPI):
    connected, loaded = await ollama_client.is_healthy()
    lessons = list_all_lesson_ids()
    if connected:
        status = "model loaded" if loaded else f"model '{settings.ollama_model}' not found — run: ollama pull {settings.ollama_model}"
        print(f"[Major Tutor] Ollama: {status}")
    else:
        print(f"[Major Tutor] WARNING: Ollama not reachable at {settings.ollama_base_url}")
    print(f"[Major Tutor] {len(lessons)} lessons loaded from courses.json")
    yield


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description=(
        "API tuteur pour MajorApp — Preparation au concours 6AF Mauritanie. "
        "Mentor IA (session, nudge, chat), TTS, STT, contenu pedagogique. "
        f"Modele: {settings.ollama_model} via Ollama."
    ),
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(mentor_router, prefix="/api/v1")
app.include_router(courses_router, prefix="/api/v1")
app.include_router(chat_router, prefix="/api/v1")
app.include_router(voice_router, prefix="/api/v1")
app.include_router(studio_router, prefix="/api/v1")


@app.get("/", tags=["Root"])
async def root():
    return {
        "name": settings.app_name,
        "version": settings.app_version,
        "docs": "/docs",
        "endpoints": {
            "mentor_session": "/api/v1/mentor/session",
            "mentor_nudge": "/api/v1/mentor/nudge",
            "mentor_question": "/api/v1/mentor/question",
            "mentor_chat": "/api/v1/mentor/chat",
            "courses": "/api/v1/courses/",
            "lesson": "/api/v1/courses/lesson/{id}",
            "studio_cahiers": "/api/v1/studio/cahiers",
            "chat": "/api/v1/chat/",
            "chat_stream": "/api/v1/chat/stream",
            "tts": "/api/v1/voice/tts",
            "stt": "/api/v1/voice/stt",
            "voice_chat": "/api/v1/voice/chat",
            "health": "/health",
        },
    }


@app.get("/health", response_model=HealthResponse, tags=["Health"])
async def health():
    connected, loaded = await ollama_client.is_healthy()
    lessons = list_all_lesson_ids()
    return HealthResponse(
        status="ok" if connected and loaded else "degraded",
        version=settings.app_version,
        ollama_connected=connected,
        model_loaded=loaded,
        courses_loaded=len(lessons),
    )
