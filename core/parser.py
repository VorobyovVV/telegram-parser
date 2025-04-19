from telethon.sync import TelegramClient
from typing import Optional, Dict
from datetime import datetime
from config.settings import settings
from utils.logger import setup_logger
import re

logger = setup_logger(__name__)

class TelegramParser:
    def __init__(self):
        self.client = TelegramClient(
            settings.SESSION_NAME,
            settings.API_ID,
            settings.API_HASH
        )

    async def parse_channel(self, channel: str):
        """Парсинг указанного канала"""
        logger.info(f"Начинаю парсинг канала: {channel}")
        
        async with self.client:
            try:
                entity = await self.client.get_entity(channel)
                async for message in self.client.iter_messages(
                    entity, 
                    limit=settings.MAX_MESSAGES
                ):
                    if not message.message:
                        continue
                        
                    post_data = self._process_message(message, channel)
                    if post_data:
                        yield post_data
                        
            except Exception as e:
                logger.error(f"Ошибка парсинга канала {channel}: {e}")

    def _process_message(self, message, channel: str) -> Optional[Dict]:
        """Обработка сообщения и извлечение данных"""
        text = message.message.lower()
        university = None
        
        for uni, patterns in settings.KEYWORDS_REGEX.items():
            if any(re.search(pattern, text) for pattern in patterns):
                university = uni
                break
                
        if not university:
            return None
            
        return {
            'id': message.id,
            'date': message.date.strftime("%Y-%m-%d %H:%M:%S"),
            'user_id': str(message.sender_id) if hasattr(message, 'sender_id') else None,
            'channel': channel,
            'message': message.message,
            'views': message.views or 0,
            'forwards': message.forwards or 0,
            'replies': message.replies.replies if message.replies else 0,
            'university': university
        }