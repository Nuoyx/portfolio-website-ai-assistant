from app.services.llm import create_llm
from uuid import UUID, uuid4
from app.repositories.conversation_repository import (
    ConversationRepository,
)
from langchain_core.messages import HumanMessage

class ChatService:

    def __init__(
            self,
            conversation_repository: ConversationRepository
    ):
        self.llm = create_llm()
        self.conversation_repository = conversation_repository

    @staticmethod
    def _extract_text(content: str | list) -> str:
        if isinstance(content, str):
            return content

        if isinstance(content, list):
            text_parts: list[str] = []

            for block in content:
                if isinstance(block, str):
                    text_parts.append(block)

                elif isinstance(block, dict):
                    text = block.get("text")

                    if isinstance(text, str):
                        text_parts.append(text)

            return "".join(text_parts)

        return str(content)
    async def process_message(
        self,
        message: str,
        conversation_id: UUID | None = None,
    ) -> tuple[UUID, str]:

        if conversation_id is None:
            conversation_id = uuid4()

        history = await self.conversation_repository.get_messages(
            conversation_id
        )

        user_message = HumanMessage(content=message)

        messages = history + [user_message]

        response = await self.llm.ainvoke(messages)

        updated_messages = messages + [response]

        await self.conversation_repository.save_messages(
            conversation_id,
            updated_messages,
        )

        answer = self._extract_text(response.content)

        return conversation_id, answer

