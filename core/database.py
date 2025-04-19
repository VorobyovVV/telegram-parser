import sqlite3
from pathlib import Path
from config.settings import settings

class DatabaseManager:
    def __init__(self):
        settings.DB_PATH.parent.mkdir(exist_ok=True)
        self.conn = sqlite3.connect(settings.DB_PATH)
        self._init_db()

    def _init_db(self):
        """Инициализация структуры БД"""
        cursor = self.conn.cursor()
        cursor.executescript("""
            CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY,
                date TEXT NOT NULL,
                user_id TEXT,
                channel TEXT NOT NULL,
                message TEXT NOT NULL,
                views INTEGER DEFAULT 0,
                forwards INTEGER DEFAULT 0,
                replies INTEGER DEFAULT 0,
                university TEXT NOT NULL
            );
            CREATE INDEX IF NOT EXISTS idx_university ON posts(university);
            CREATE INDEX IF NOT EXISTS idx_date ON posts(date);
        """)
        self.conn.commit()

    def save_post(self, post_data: dict):
        """Сохранение поста в БД"""
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT OR IGNORE INTO posts VALUES (
                ?, ?, ?, ?, ?, ?, ?, ?, ?
            )
        """, (
            post_data['id'],
            post_data['date'],
            post_data['user_id'],
            post_data['channel'],
            post_data['message'],
            post_data['views'],
            post_data['forwards'],
            post_data['replies'],
            post_data['university']
        ))
        self.conn.commit()

    def get_stats(self):
        """Получение статистики"""
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT 
                COUNT(*) as total_posts,
                COUNT(DISTINCT user_id) as unique_users,
                SUM(views) as total_views,
                SUM(forwards) as total_forwards,
                SUM(replies) as total_replies
            FROM posts
        """)
        return cursor.fetchone()
    
    def get_stats_by_university(self):
        """Статистика по университетам"""
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT university,
                   COUNT(*) as total_posts,
                   COUNT(DISTINCT user_id) as unique_users,
                   SUM(views) as total_views,
                   SUM(forwards) as total_forwards,
                   SUM(replies) as total_replies
            FROM posts
            GROUP BY university
        """)
        return cursor.fetchall()

    def get_daily_post_counts(self):
        """Количество публикаций по дням"""
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT date(date) as day, COUNT(*) as count
            FROM posts
            GROUP BY day
            ORDER BY day
        """)
        return cursor.fetchall()

    def close(self):
        """Закрытие соединения с БД"""
        self.conn.close()