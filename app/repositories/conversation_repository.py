import json
from uuid import UUID

from redis.asyncio import Redis
from langchain_core.messages import BaseMessage, messages_from_dict, messages_to_dict

from app.core.config import get_settings


class ConversationRepository:
    def __init__(self) -> None:
        settings = get_settings()

        self.redis: Redis = Redis.from_url(
            settings.redis_url,
            decode_responses=True,
        )

        self.ttl = settings.redis_ttl_seconds

    def _get_key(self, conversation_id: UUID) -> str:
        return f"conversation:{conversation_id}"

    async def get_messages(
        self,
        conversation_id: UUID,
    ) -> list[BaseMessage]:
        key = self._get_key(conversation_id)

        data = await self.redis.get(key)

        if data is None:
            return []

        serialized_messages = json.loads(data)

        return messages_from_dict(serialized_messages)

    async def save_messages(
        self,
        conversation_id: UUID,
        messages: list[BaseMessage],
    ) -> None:
        key = self._get_key(conversation_id)

        serialized_messages = messages_to_dict(messages)

        await self.redis.set(
            key,
            json.dumps(serialized_messages),
            ex=self.ttl,
        )

    async def delete_messages(
        self,
        conversation_id: UUID,
    ) -> None:
        key = self._get_key(conversation_id)

        await self.redis.delete(key)

    async def close(self) -> None:
        await self.redis.aclose()

