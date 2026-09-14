from langchain_google_genai import ChatGoogleGenerativeAI

from app.core.config import get_settings


def create_llm() -> ChatGoogleGenerativeAI:
    settings = get_settings()

    return ChatGoogleGenerativeAI(
        model=settings.gemini_model,
        api_key=settings.gemini_api_key,
    )