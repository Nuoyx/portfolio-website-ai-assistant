from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    message: str = Field(
        ...,
        min_length=1,
        max_length=2000,
        description="User's message",
    )

    conversation_id: str = Field(
        ...,
        min_length=1,
        description="Temporary conversation identifier",
    )


class ChatResponse(BaseModel):
    conversation_id: str
    answer: str

