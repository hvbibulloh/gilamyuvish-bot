from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admin_exit = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Chiqish')
        ]
    ]
)

ishchilar_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Ro'yxatga olish 📝")
        ]
    ]
)

register_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("O'tkazib yuborish"),
            KeyboardButton("Chiqish")
        ]
    ]
)