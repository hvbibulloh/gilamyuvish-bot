from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

user_menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Kvitansiya raqamini olish 📑")
        ],
        [
            KeyboardButton("Gilamim haqida ma'lumot 🛎"),
        ],
        [
            KeyboardButton("Biz haqimizda ♻")
        ]
    ], resize_keyboard=True
)
