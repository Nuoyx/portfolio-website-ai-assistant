from fastapi import FastAPI
from app.api.chat import router as chat_router
from app.core.config import get_settings


settings = get_settings()

app = FastAPI(
    title="Portfolio AI Assistant",
    version="1.0.0",
)

app.include_router(chat_router)

@app.get("/health")
async def health_check():
    return {
        "status": "ok",
        "service": settings.app_name,
    }
