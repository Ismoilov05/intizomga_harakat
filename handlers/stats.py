from aiogram import Router, types, F
from aiogram.types import FSInputFile
from db import get_connection
import matplotlib.pyplot as plt

router = Router()

@router.message(F.text == "📊 Statistikani ko‘rish")
async def show_stats(msg: types.Message):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT date, focus_score FROM reports
        WHERE user_id = ? ORDER BY date DESC LIMIT 7
    """, (msg.from_user.id,))
    data = cur.fetchall()
    conn.close()

    if not data:
        await msg.answer("Hozircha hisobot topilmadi 😅 /report orqali bir nechta kunlik ma'lumot yubor.")
        return

    # Ma'lumotlarni teskari tartibda chiqaramiz
    data.reverse()
    dates = [row[0][-5:] for row in data]  # faqat oy-kun qismini olamiz
    scores = [row[1] for row in data]

    # Grafik chizish
    plt.figure()
    plt.plot(dates, scores, marker='o')
    plt.title("📊 7 kunlik intizom darajasi")
    plt.xlabel("Sana")
    plt.ylabel("Ball (1–10)")
    plt.ylim(0, 10)
    plt.grid(True)

    # Grafikni saqlash
    path = f"stats_{msg.from_user.id}.png"
    plt.savefig(path)
    plt.close()

    # Grafikni yuborish
    photo = FSInputFile(path)
    await msg.answer_photo(photo, caption="Sening 7 kunlik intizoming 📈")
