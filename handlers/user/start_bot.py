from aiogram import types

from keyboard.user.menu_key import user_menu_keyboard
from loader import dp
import config as cfg


@dp.message_handler(commands=['start'])
async def startbot(message: types.Message):
    await message.answer('Assalomu aleykum Sof gilam yuvish markazining botiga xush kelibsiz',
                         reply_markup=user_menu_keyboard)


@dp.message_handler(text="Kvitansiya raqamini olish 📑")
async def kvitansiya(message: types.Message):
    await message.answer("Telefon raqamingizni yuboring 📱 \n\n(Ma'lumot to'ldirganda bergan raqamingizni kiriting ❗)")