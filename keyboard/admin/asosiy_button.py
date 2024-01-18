from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import db


def asosiy_button(id):
    buttons = db.get_mijoz(id)
    btn = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
    orqaga = KeyboardButton("Chiqish")

    btn.add(orqaga)

    for i in range(1, int(buttons) + 1):
        btn.add(f"Gilam - {i}")
    return btn


def parda_button(id):
    buttons = db.get_parda(id)
    btn = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
    orqaga = KeyboardButton("Chiqish")

    btn.add(orqaga)
    for i in range(1, int(buttons) + 1):
        btn.add(f"Parda - {i}")
    return btn


def korpa_button(id):
    buttons = db.get_korpa(id)
    btn = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
    orqaga = KeyboardButton("Chiqish")

    btn.add(orqaga)
    for i in range(1, int(buttons) + 1):
        btn.add(f"Korpa - {i}")

    return btn


def yostiq_button(id):
    buttons = db.get_yostiq(id)
    btn = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
    orqaga = KeyboardButton("Chiqish")
    btn.add(orqaga)
    for i in range(1, int(buttons) + 1):
        btn.add(f"Yostiq - {i}")

    return btn
