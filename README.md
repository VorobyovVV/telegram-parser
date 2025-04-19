# 📡 Telegram Parser

Этот проект предназначен для парсинга Telegram-каналов с помощью библиотеки [Telethon](https://github.com/LonamiWebs/Telethon). Парсер извлекает сообщения из 500 последних постов, содержащие упоминания университетов (СПбГУ, МГУ), сохраняет данные в SQLite и строит статистику.

## 🚀 Возможности

- Поиск сообщений по регулярным выражениям.
- Сохранение результатов в SQLite-базу.
- Логирование в файл.
- Сбор статистики по упоминаниям университетов.
- Построение графика количества публикаций по дням.

## 🏗 Структура проекта

```
telegram_parser/
├── config/           # Настройки
├── core/             # Логика парсинга и работа с БД
├── utils/            # Логгер и вспомогательные утилиты
├── data/             # SQLite-база данных
├── logs/             # Логи
├── main.py           # Точка входа
├── .env              # Переменные окружения
├── .gitignore
├── requirements.txt
└── README.md
```

## ⚙️ Установка и запуск

### 1. Клонируй репозиторий

```bash
git clone [https://github.com/yourusername/telegram_parser.git](https://github.com/VorobyovVV/telegram-parser.git)
cd telegram_parser
```

### 2. Установи зависимости

```bash
pip install -r requirements.txt
```

### 3. Настрой `.env`

Создай файл `.env` в корне проекта и добавь:

```env
API_ID=your_telegram_api_id
API_HASH=your_telegram_api_hash
SESSION_NAME=telegram_session
MAX_MESSAGES=1000
```

Зарегистрировать `API_ID` и `API_HASH` можно на [my.telegram.org](https://my.telegram.org).

### 4. Запуск парсера

```bash
python main.py <список_каналов>
```

Например:

```bash
python main.py @spbuniversity @naukamsu
```

### 5. Авторизация телеграмма

```bash
Введите номер:
Введите код для входа:
Введите пароль:
```
По завершении парсинга будет выведена статистика, а также сохранится график в `daily_posts.png`.

## 📊 Пример результата

```
📊 Результаты парсинга по университетам:

🏫 СПбГУ:
• Публикаций: 53
• Уникальных пользователей: 42
• Просмотров: 10421
• Репостов: 120
• Комментариев: 13

🏫 МГУ:
• Публикаций: 31
• Уникальных пользователей: 28
• Просмотров: 8912
• Репостов: 87
• Комментариев: 5

📈 График сохранён в файл: daily_posts.png
```

## 📁 Файлы логов

Все события записываются в `logs/parser.log`.

## 📌 Зависимости

- [Telethon](https://github.com/LonamiWebs/Telethon)
- [python-dotenv](https://github.com/theskumar/python-dotenv)
- [matplotlib](https://matplotlib.org/)

