from fastapi import APIRouter, Depends

from app.models.chat import ChatRequest, ChatResponse
from app.services.chat_service import ChatService
from app.repositories.conversation_repository import (
    ConversationRepository,
)


router = APIRouter(
    prefix="/api/chat",
    tags=["Chat"],
)

conversation_repository = ConversationRepository()


def get_conversation_repository() -> ConversationRepository:
    return conversation_repository

def get_chat_service(
    repository: ConversationRepository = Depends(
        get_conversation_repository
    ),
) -> ChatService:
    return ChatService(
        conversation_repository=repository,
    )


@router.post("", response_model=ChatResponse)
async def chat(
    request: ChatRequest,
    chat_service: ChatService = Depends(get_chat_service),
) -> ChatResponse:
    conversation_id, answer = await chat_service.process_message(
        message=request.message,
        conversation_id=request.conversation_id,
    )

    return ChatResponse(
        conversation_id=conversation_id,
        answer=answer,
    )

