from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.studio import router as studio_router


app = FastAPI(
    title="Major Cahier Studio API",
    version="1.0.0",
    description="API legere pour editer les cahiers HTML Major et regenerer les PDF.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(studio_router, prefix="/api/v1")


@app.get("/health", tags=["Health"])
async def health():
    return {"status": "ok", "service": "studio"}
