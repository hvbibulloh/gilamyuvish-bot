from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admin_exit = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Chiqish')
        ]
    ], resize_keyboard=True
)

ishchilar_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Ro'yxatga olish 📝")
        ]
    ], resize_keyboard=True
)

register_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("O'tkazib yuborish"),
            KeyboardButton("Chiqish")
        ]
    ], resize_keyboard=True
)