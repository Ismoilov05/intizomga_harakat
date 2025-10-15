from aiogram import Router, types, F
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from db import add_report
import datetime

router = Router()

class ReportForm(StatesGroup):
    focus_score = State()
    comment = State()

@router.message(F.text == "📝 Bugungi hisobotni yuborish")
async def start_report(msg: types.Message, state: FSMContext):
    await msg.answer("Bugungi intizomingni 1 dan 10 gacha bahola:")
    await state.set_state(ReportForm.focus_score)

@router.message(ReportForm.focus_score)
async def process_score(msg: types.Message, state: FSMContext):
    try:
        score = int(msg.text)
        if not 1 <= score <= 10:
            raise ValueError
    except ValueError:
        await msg.answer("❗ 1 dan 10 gacha son kiriting.")
        return

    await state.update_data(focus_score=score)
    await msg.answer("Qisqacha yoz: bugun nimalarni uddalading?")
    await state.set_state(ReportForm.comment)

@router.message(ReportForm.comment)
async def process_comment(msg: types.Message, state: FSMContext):
    data = await state.get_data()
    focus_score = data["focus_score"]
    comment = msg.text
    add_report(msg.from_user.id, str(datetime.date.today()), focus_score, comment)
    await msg.answer("✅ Hisoboting saqlandi! Barakalla 💪")
    await state.clear()
