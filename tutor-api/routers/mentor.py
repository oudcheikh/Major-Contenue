import json

from fastapi import APIRouter, HTTPException

from models import (
    MentorSessionRequest,
    MentorSessionResponse,
    MicroChallenge,
    NudgeRequest,
    NudgeResponse,
    QuestionRequest,
    QuestionResponse,
    MentorChatRequest,
    MentorChatResponse,
)
from services.llm import ollama_client
from services.knowledge import build_lesson_context, find_lesson
from prompts.tutor import (
    build_session_prompt,
    build_nudge_prompt,
    build_question_prompt,
    build_chat_prompt,
)

router = APIRouter(prefix="/mentor", tags=["Mentor"])


def _parse_session_json(raw: str) -> dict:
    """Extract and parse JSON from LLM output, handling markdown fences."""
    cleaned = raw.strip()
    if cleaned.startswith("```"):
        cleaned = cleaned.split("\n", 1)[-1]
    if cleaned.endswith("```"):
        cleaned = cleaned.rsplit("```", 1)[0]
    cleaned = cleaned.strip()

    start = cleaned.find("{")
    end = cleaned.rfind("}")
    if start >= 0 and end > start:
        cleaned = cleaned[start : end + 1]

    return json.loads(cleaned)


@router.post("/session", response_model=MentorSessionResponse)
async def generate_session(request: MentorSessionRequest):
    """Generate a full mentor session (hook + summary + quiz) for a lesson."""
    lesson = find_lesson(request.lesson_id)
    if not lesson:
        raise HTTPException(status_code=404, detail=f"Lesson '{request.lesson_id}' not found")

    context = build_lesson_context(request.lesson_id)
    messages = build_session_prompt(context, request.student_name)

    try:
        result = await ollama_client.raw_chat(messages)
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"LLM error: {e}")

    try:
        parsed = _parse_session_json(result["reply"])
    except (json.JSONDecodeError, KeyError) as e:
        raise HTTPException(
            status_code=500,
            detail=f"LLM returned invalid JSON. Raw: {result['reply'][:300]}",
        )

    if not all(k in parsed for k in ("hook", "summaryPoints", "microChallenge")):
        raise HTTPException(status_code=500, detail="LLM response missing required fields")

    mc = parsed["microChallenge"]
    return MentorSessionResponse(
        hook=parsed["hook"],
        summaryPoints=parsed["summaryPoints"][:3],
        microChallenge=MicroChallenge(
            question=mc.get("question", ""),
            options=mc.get("options", [])[:4],
            correctIndex=mc.get("correctIndex", 0),
            hint=mc.get("hint", ""),
        ),
        lesson_id=request.lesson_id,
        model=result["model"],
    )


@router.post("/nudge", response_model=NudgeResponse)
async def generate_nudge(request: NudgeRequest):
    """Give feedback on a quiz answer without revealing the answer."""
    lesson = find_lesson(request.lesson_id)
    if not lesson:
        raise HTTPException(status_code=404, detail=f"Lesson '{request.lesson_id}' not found")

    context = build_lesson_context(request.lesson_id)
    messages = build_nudge_prompt(
        context,
        request.question,
        request.selected_option,
        request.is_correct,
        request.attempts,
        request.student_name,
    )

    try:
        result = await ollama_client.raw_chat(messages)
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"LLM error: {e}")

    return NudgeResponse(feedback=result["reply"], model=result["model"])


@router.post("/question", response_model=QuestionResponse)
async def answer_question(request: QuestionRequest):
    """Answer a student's question about a lesson topic."""
    lesson = find_lesson(request.lesson_id)
    if not lesson:
        raise HTTPException(status_code=404, detail=f"Lesson '{request.lesson_id}' not found")

    context = build_lesson_context(request.lesson_id)
    messages = build_question_prompt(context, request.question, request.student_name)

    try:
        result = await ollama_client.raw_chat(messages)
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"LLM error: {e}")

    return QuestionResponse(answer=result["reply"], model=result["model"])


@router.post("/chat", response_model=MentorChatResponse)
async def mentor_chat(request: MentorChatRequest):
    """Free-form chat with the mentor about a lesson."""
    lesson = find_lesson(request.lesson_id)
    if not lesson:
        raise HTTPException(status_code=404, detail=f"Lesson '{request.lesson_id}' not found")

    context = build_lesson_context(request.lesson_id)
    history = [{"role": m.role, "content": m.content} for m in request.conversation_history]
    messages = build_chat_prompt(context, request.message, history, request.student_name)

    try:
        result = await ollama_client.raw_chat(messages)
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"LLM error: {e}")

    return MentorChatResponse(reply=result["reply"], model=result["model"])
