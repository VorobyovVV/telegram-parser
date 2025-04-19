import asyncio
import argparse
import matplotlib.pyplot as plt
from core.parser import TelegramParser
from core.database import DatabaseManager
from utils.logger import setup_logger

logger = setup_logger(__name__)

def plot_daily_posts(daily_counts):
    dates = [row[0] for row in daily_counts]
    counts = [row[1] for row in daily_counts]

    plt.figure(figsize=(10, 5))
    plt.plot(dates, counts, marker='o')
    plt.title('Количество публикаций в день')
    plt.xlabel('Дата')
    plt.ylabel('Количество постов')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('daily_posts.png')

async def main(channels: list):
    db = DatabaseManager()
    parser = TelegramParser()
    
    for channel in channels:
        async for post in parser.parse_channel(channel):
            db.save_post(post)
            logger.info(f"Сохранен пост {post['id']} из {channel}")

    stats = db.get_stats_by_university()
    daily_counts = db.get_daily_post_counts()

    print("\n📊 Результаты парсинга по университетам:")
    for row in stats:
        university, total_posts, unique_users, views, forwards, replies = row
        print(f"\n🏫 {university}:")
        print(f"• Публикаций: {total_posts}")
        print(f"• Уникальных пользователей: {unique_users}")
        print(f"• Просмотров: {views or 0}")
        print(f"• Репостов: {forwards or 0}")
        print(f"• Комментариев: {replies or 0}")

    plot_daily_posts(daily_counts)
    print("\n📈 График сохранён в файл: daily_posts.png")

    db.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('channels', nargs='+', help='Telegram каналы для парсинга')
    args = parser.parse_args()
    
    asyncio.run(main(args.channels))
