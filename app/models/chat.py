from pydantic import BaseModel, Field
from uuid import UUID


class ChatRequest(BaseModel):
    message: str = Field(
        ...,
        min_length=1,
        max_length=2000,
        description="User's message",
    )

    conversation_id: UUID | None = None


class ChatResponse(BaseModel):
    conversation_id: UUID
    answer: str

