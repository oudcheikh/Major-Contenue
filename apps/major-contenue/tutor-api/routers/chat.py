from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field
from typing import Optional

from services.llm import ollama_client

router = APIRouter(prefix="/chat", tags=["Chat (generic)"])


class GenericChatMessage(BaseModel):
    role: str = Field(..., pattern="^(user|assistant)$")
    content: str


class GenericChatRequest(BaseModel):
    message: str
    lang: str = "fr"
    subject: Optional[str] = None
    lesson_context: Optional[str] = None
    conversation_history: list[GenericChatMessage] = Field(default_factory=list)


@router.post("/")
async def chat(request: GenericChatRequest):
    """Generic chat endpoint (free-form, not tied to a specific lesson)."""
    try:
        result = await ollama_client.chat(
            user_message=request.message,
            lang=request.lang,
            subject=request.subject,
            lesson_context=request.lesson_context,
            history=request.conversation_history,
        )
        return {"reply": result["reply"], "model": result["model"], "usage": result["usage"]}
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Ollama error: {e}")


@router.post("/stream")
async def chat_stream(request: GenericChatRequest):
    """Generic chat with Server-Sent Events streaming."""

    async def event_generator():
        try:
            async for token in ollama_client.chat_stream(
                user_message=request.message,
                lang=request.lang,
                subject=request.subject,
                lesson_context=request.lesson_context,
                history=request.conversation_history,
            ):
                yield f"data: {token}\n\n"
            yield "data: [DONE]\n\n"
        except Exception as e:
            yield f"data: [ERROR] {e}\n\n"

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )
