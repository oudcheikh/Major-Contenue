import io
import tempfile
from pathlib import Path

from faster_whisper import WhisperModel

from config import settings


class STTService:
    """Speech-to-Text using faster-whisper (CTranslate2 Whisper)."""

    def __init__(self):
        self._model: WhisperModel | None = None

    def _get_model(self) -> WhisperModel:
        if self._model is None:
            self._model = WhisperModel(
                settings.whisper_model_size,
                device=settings.whisper_device,
                compute_type=settings.whisper_compute_type,
            )
        return self._model

    async def transcribe(self, audio_bytes: bytes, language: str | None = None) -> dict:
        """
        Transcribe audio bytes to text.
        Accepts any format ffmpeg supports (mp3, wav, ogg, webm, m4a...).
        """
        model = self._get_model()

        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
            f.write(audio_bytes)
            tmp_path = f.name

        try:
            segments, info = model.transcribe(
                tmp_path,
                language=language if language in ("ar", "fr") else None,
                beam_size=5,
                vad_filter=True,
            )
            text = " ".join(seg.text.strip() for seg in segments)
        finally:
            Path(tmp_path).unlink(missing_ok=True)

        return {
            "text": text,
            "language": info.language,
            "language_probability": round(info.language_probability, 3),
            "duration_seconds": round(info.duration, 2),
        }


stt_service = STTService()
