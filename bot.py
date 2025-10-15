import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import start, daily_task, report, stats
from Utils import scheduler
from db import init_db

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    init_db()

    dp.include_router(start.router)
    dp.include_router(daily_task.router)
    dp.include_router(report.router)
    dp.include_router(stats.router)

    print("Bot is running with scheduler ⏰ and motivation 💡...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
