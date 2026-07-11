from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Major Tutor API"
    app_version: str = "1.0.0"

    ollama_base_url: str = "http://localhost:11434"
    ollama_model: str = "qwen2.5:1.5b"
    ollama_timeout: int = 300

    default_lang: str = "ar"

    # STT (faster-whisper)
    whisper_model_size: str = "base"
    whisper_device: str = "cpu"
    whisper_compute_type: str = "int8"

    # TTS (edge-tts)
    tts_voice_ar: str = "ar-SA-HamedNeural"
    tts_voice_fr: str = "fr-FR-HenriNeural"

    # Limites
    max_conversation_turns: int = 50
    max_audio_duration_seconds: int = 60

    class Config:
        env_file = ".env"
        env_prefix = "TUTOR_"


settings = Settings()
