from fastapi import APIRouter, Depends

from app.models.chat import ChatRequest, ChatResponse
from app.services.chat_service import ChatService


router = APIRouter(
    prefix="/api/chat",
    tags=["Chat"],
)


def get_chat_service() -> ChatService:
    return ChatService()


@router.post("", response_model=ChatResponse)
async def chat(
    request: ChatRequest,
    chat_service: ChatService = Depends(get_chat_service),
):

    conversation_id, answer = await chat_service.process_message(
        message=request.message,
        conversation_id=request.conversation_id,
    )

    return ChatResponse(
        conversation_id=conversation_id,
        answer=answer,
    )

