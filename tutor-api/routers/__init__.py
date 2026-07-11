from .chat import router as chat_router
from .voice import router as voice_router
from .mentor import router as mentor_router
from .courses import router as courses_router
from .studio import router as studio_router

__all__ = ["chat_router", "voice_router", "mentor_router", "courses_router", "studio_router"]
