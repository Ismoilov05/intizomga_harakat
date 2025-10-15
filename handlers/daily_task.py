from aiogram import Router, types, F
import datetime

router = Router()

@router.message(F.text == "🧠 Bugungi topshiriq")
async def send_daily_task(msg: types.Message):
    day = datetime.date.today().strftime("%A")
    tasks = {
        "Monday": "🧠 O‘zingni kuzat: bugun nechta marta chalg‘iding?",
        "Tuesday": "🕒 Rejalashtir: bugungi 3 asosiy maqsadingni yoz.",
        "Wednesday": "🔥 Yo‘qimli bo‘lmagan ishni bajargin.",
        "Thursday": "🎯 Pomodoro bilan ishlang (3 ta sikl).",
        "Friday": "🏃 10 daqiqa jismoniy mashq.",
        "Saturday": "🧘‍♂️ 10 daqiqa tinch o‘tirish (meditatsiya).",
        "Sunday": "📊 Hisobot haftasi — o‘zingni bahola."
    }
    task = tasks.get(day, "Bugun intizomli bo‘l! 💪")
    await msg.answer(task)
