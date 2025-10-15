from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

router = Router()

# --- Asosiy menyu ---
main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🧠 Bugungi topshiriq")],
        [KeyboardButton(text="📝 Bugungi hisobotni yuborish")],
        [KeyboardButton(text="📊 Statistikani ko‘rish")],
    ],
    resize_keyboard=True,  # tugmalar ekranga moslashadi
    one_time_keyboard=False  # menyu doim ko‘rinib turadi
)

# --- /start komandasi ---
@router.message(CommandStart())
async def start_handler(msg: types.Message):
    text = (
        f"Salom, {msg.from_user.first_name}! 👋\n\n"
        "Bu bot intizomingni oshirishga yordam beradi 💪\n"
        "Quyidagilardan birini tanla:\n"
        "🧠 - bugungi vazifa\n"
        "📝 - bugungi hisobot\n"
        "📊 - o‘tgan kunlar statistikasi\n\n"
        "Boshlaymizmi? 🚀"
    )

    await msg.answer(text, reply_markup=main_menu)
