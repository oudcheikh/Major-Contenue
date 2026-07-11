import httpx
from typing import AsyncGenerator

from config import settings
from prompts import get_tutor_prompt


class OllamaClient:
    """Client for Ollama LLM API."""

    def __init__(self):
        self.base_url = settings.ollama_base_url
        self.model = settings.ollama_model
        self.timeout = settings.ollama_timeout

    def _build_messages(
        self,
        user_message: str,
        lang: str,
        subject: str | None = None,
        lesson_context: str | None = None,
        history: list | None = None,
    ) -> list[dict]:
        system_prompt = get_tutor_prompt(lang)

        if subject:
            system_prompt += f"\n\nMatiere actuelle : {subject}"
        if lesson_context:
            system_prompt += f"\n\nContexte : {lesson_context}"

        messages = [{"role": "system", "content": system_prompt}]

        if history:
            for msg in history:
                role = msg.role if hasattr(msg, "role") else msg.get("role", "user")
                content = msg.content if hasattr(msg, "content") else msg.get("content", "")
                messages.append({"role": role, "content": content})

        messages.append({"role": "user", "content": user_message})
        return messages

    async def chat(
        self,
        user_message: str,
        lang: str = "ar",
        subject: str | None = None,
        lesson_context: str | None = None,
        history: list | None = None,
    ) -> dict:
        messages = self._build_messages(user_message, lang, subject, lesson_context, history)

        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response = await client.post(
                f"{self.base_url}/api/chat",
                json={"model": self.model, "messages": messages, "stream": False},
            )
            response.raise_for_status()
            data = response.json()

        return {
            "reply": data["message"]["content"],
            "model": data.get("model", self.model),
            "usage": {
                "prompt_tokens": data.get("prompt_eval_count", 0),
                "completion_tokens": data.get("eval_count", 0),
                "total_duration_ms": data.get("total_duration", 0) // 1_000_000,
            },
        }

    async def chat_stream(
        self,
        user_message: str,
        lang: str = "ar",
        subject: str | None = None,
        lesson_context: str | None = None,
        history: list | None = None,
    ) -> AsyncGenerator[str, None]:
        messages = self._build_messages(user_message, lang, subject, lesson_context, history)

        async with httpx.AsyncClient(timeout=self.timeout) as client:
            async with client.stream(
                "POST",
                f"{self.base_url}/api/chat",
                json={"model": self.model, "messages": messages, "stream": True},
            ) as response:
                response.raise_for_status()
                async for line in response.aiter_lines():
                    if line:
                        import json
                        chunk = json.loads(line)
                        token = chunk.get("message", {}).get("content", "")
                        if token:
                            yield token
                        if chunk.get("done", False):
                            break

    async def raw_chat(self, messages: list[dict]) -> dict:
        """Send pre-built messages directly to Ollama. Used by mentor endpoints."""
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response = await client.post(
                f"{self.base_url}/api/chat",
                json={"model": self.model, "messages": messages, "stream": False},
            )
            response.raise_for_status()
            data = response.json()

        return {
            "reply": data["message"]["content"],
            "model": data.get("model", self.model),
        }

    async def is_healthy(self) -> tuple[bool, bool]:
        """Returns (ollama_connected, model_loaded)."""
        try:
            async with httpx.AsyncClient(timeout=5) as client:
                resp = await client.get(f"{self.base_url}/api/tags")
                resp.raise_for_status()
                models = [m["name"] for m in resp.json().get("models", [])]
                model_loaded = any(self.model in m for m in models)
                return True, model_loaded
        except Exception:
            return False, False


ollama_client = OllamaClient()
