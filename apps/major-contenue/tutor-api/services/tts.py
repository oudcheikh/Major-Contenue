import base64
import io
import edge_tts

from config import settings


class TTSService:
    """Text-to-Speech using edge-tts (free Microsoft Edge voices)."""

    VOICES = {
        "ar": settings.tts_voice_ar,
        "fr": settings.tts_voice_fr,
    }

    async def synthesize(self, text: str, lang: str = "ar") -> bytes:
        voice = self.VOICES.get(lang, self.VOICES["ar"])
        communicate = edge_tts.Communicate(text, voice)

        audio_buffer = io.BytesIO()
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio_buffer.write(chunk["data"])

        return audio_buffer.getvalue()

    async def synthesize_base64(self, text: str, lang: str = "ar") -> str:
        audio_bytes = await self.synthesize(text, lang)
        return base64.b64encode(audio_bytes).decode("utf-8")

    @staticmethod
    async def list_voices(lang_prefix: str = "ar") -> list[dict]:
        voices = await edge_tts.list_voices()
        return [
            {"name": v["ShortName"], "gender": v["Gender"], "locale": v["Locale"]}
            for v in voices
            if v["Locale"].startswith(lang_prefix)
        ]


tts_service = TTSService()
