from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import db


def asosiy_button(id):
    buttons = db.get_mijoz(id)
    btn = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
    orqaga = KeyboardButton("Chiqish")

    btn.add(orqaga)
    for i in range(1, int(buttons[0]) + 1):
        btn.add(f"Gilam - {i}")
    return btn
