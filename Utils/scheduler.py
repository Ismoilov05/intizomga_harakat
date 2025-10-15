import aiocron
from aiogram import Bot
from db import get_connection
from Utils.quotes import get_random_quote

# Ertalabki eslatma (08:00)
@aiocron.crontab('0 8 * * *')
async def morning_task():
    bot = Bot.from_current()
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT user_id FROM reports")
    users = cur.fetchall()
    conn.close()

    quote = get_random_quote()

    for user in users:
        user_id = user[0]
        await bot.send_message(
            chat_id=user_id,
            text=f"🌅 *Yangi kun, yangi intizom!*\n\n{quote}\n\nBugungi topshiriqni /task buyrug‘i orqali ko‘r.",
            parse_mode="Markdown"
        )
