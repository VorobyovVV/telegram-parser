from pathlib import Path
from dotenv import load_dotenv
import os
import re 

load_dotenv()

class Settings:
    # Telegram API
    API_ID = int(os.getenv('API_ID'))
    API_HASH = os.getenv('API_HASH')
    SESSION_NAME = os.getenv('SESSION_NAME', 'telegram_session')
    
    # Параметры парсинга
    MAX_MESSAGES = int(os.getenv('MAX_MESSAGES', 500))
    # Ключевые слова в виде регулярных выражений
    KEYWORDS_REGEX = {
        'СПбГУ': [
            r'\bспбгу\b',
            r'\bspbu\b',
            r'санкт[\s-]*петербург(ский)?[\s-]*университет'
        ],
        'МГУ': [
            r'\bмгу\b',
            r'\bmsu\b',
            r'московск(ий|ого)?[\s-]*университет'
        ]
    }
    
    # Пути
    BASE_DIR = Path(__file__).parent.parent
    DB_PATH = BASE_DIR / 'data' / 'web2_telegram.db'
    LOGS_DIR = BASE_DIR / 'logs'

settings = Settings()