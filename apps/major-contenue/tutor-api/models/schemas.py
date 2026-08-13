from pydantic import BaseModel, Field
from typing import Optional


# --- Mentor schemas (MajorApp-compatible) ---

class MentorSessionRequest(BaseModel):
    lesson_id: str
    student_name: str = "Eleve"


class MicroChallenge(BaseModel):
    question: str
    options: list[str]
    correctIndex: int
    hint: str


class MentorSessionResponse(BaseModel):
    hook: str
    summaryPoints: list[str]
    microChallenge: MicroChallenge
    lesson_id: str
    model: str


class NudgeRequest(BaseModel):
    lesson_id: str
    question: str
    selected_option: str
    is_correct: bool
    attempts: int = 1
    student_name: str = "Eleve"


class NudgeResponse(BaseModel):
    feedback: str
    model: str


class QuestionRequest(BaseModel):
    lesson_id: str
    question: str
    student_name: str = "Eleve"


class QuestionResponse(BaseModel):
    answer: str
    model: str


class ChatMessage(BaseModel):
    role: str = Field(..., pattern="^(user|assistant)$")
    content: str


class MentorChatRequest(BaseModel):
    lesson_id: str
    message: str
    student_name: str = "Eleve"
    conversation_history: list[ChatMessage] = Field(default_factory=list)


class MentorChatResponse(BaseModel):
    reply: str
    model: str


# --- Voice schemas ---

class TTSRequest(BaseModel):
    text: str
    lang: str = "fr"


class TTSResponse(BaseModel):
    audio_base64: str
    format: str = "mp3"
    lang: str


class VoiceChatResponse(BaseModel):
    transcript: str
    reply_text: str
    reply_audio_base64: str
    audio_format: str = "mp3"
    model: str


# --- Health ---

class HealthResponse(BaseModel):
    status: str
    version: str
    ollama_connected: bool
    model_loaded: bool
    courses_loaded: int
