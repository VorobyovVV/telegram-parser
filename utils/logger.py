import logging
from pathlib import Path
from config.settings import settings

def setup_logger(name: str) -> logging.Logger:
    """Настройка логгера"""
    settings.LOGS_DIR.mkdir(exist_ok=True)
    
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # Логирование в файл
    file_handler = logging.FileHandler(settings.LOGS_DIR / 'parser.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Вывод в консоль
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger