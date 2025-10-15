import random

QUOTES = [
    "“Intizom — bu erkinlik sari yo‘l.” — Epiktet",
    "“Hech kim har doim motivatsiyalangan bo‘la olmaydi, lekin intizomli odam shunday bo‘lib ko‘rinadi.”",
    "“Senga yoqmasa ham, o‘zing uchun kerak bo‘lgan ishni qil.”",
    "“Kichik tartib — katta natijaning onasi.”",
    "“Har bir buyuklik — kundalik odat natijasi.”",
    "“Intizom — bu o‘zingni sevimli odamdek boshqarishdir.”",
    "“Erta uyg‘on, o‘zingni yeng — dunyo shunda sen uchun ochiladi.”",
]

def get_random_quote():
    return random.choice(QUOTES)
