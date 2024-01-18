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
            KeyboardButton("Ro'yxatga olish 📝"),

        ],
        [
            KeyboardButton("Gilam Yuvish 🚿"),
            KeyboardButton("Gilam Tayyor ✅")
        ],
        [
            KeyboardButton("Hammasini Yuvish 🚿"),
            KeyboardButton("Hammasi Tayyor ✅")
        ],
        [
            KeyboardButton("Pardozlash 🧴"),
        ],
        [
            KeyboardButton("Tekshirish 🔍")
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

yes_or_no_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Ha ✅"),
            KeyboardButton("Yo'q ⛔ Boshqa maxsulot kiritmayman")
        ]
    ], resize_keyboard=True
)
hammasi_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Ko'rpa"),
            KeyboardButton("Parda"),
            KeyboardButton("Yostiq")
        ]
    ], resize_keyboard=True
)
