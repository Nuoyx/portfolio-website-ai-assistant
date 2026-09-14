from app.services.llm import create_llm


class ChatService:

    def __init__(self):
        self.llm = create_llm()

    async def process_message(
        self,
        message: str,
        conversation_id: str,
    ) -> str:

        response = await self.llm.ainvoke(message)

        return response.content

