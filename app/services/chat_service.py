from app.services.llm import create_llm
from uuid import UUID, uuid4

class ChatService:

    def __init__(self):
        self.llm = create_llm()

    async def process_message(
        self,
        message: str,
        conversation_id: UUID | None = None,
    ) -> tuple[UUID, str]:

        if conversation_id is None:
            conversation_id = uuid4()

        response = await self.llm.ainvoke(message)

        return conversation_id, response.content

