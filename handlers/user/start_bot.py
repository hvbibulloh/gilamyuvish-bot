from datetime import datetime

from aiogram import types

from keyboard.admin.admin_keys import ishchilar_keyboard
from keyboard.user.menu_key import user_menu_keyboard
from loader import dp
import config as cfg


@dp.message_handler(commands=['start'])
async def startbot(message: types.Message):
    if message.from_user.id in cfg.ISHCHI:
        current_time = datetime.now()
        await message.answer(
            f"Assalomu Aleykum {message.from_user.full_name} \n\nSoat: {current_time.hour}:{current_time.minute}\nKuningiz yaxshi o'tsin ☺",
            reply_markup=ishchilar_keyboard)

    if message.from_user.id in cfg.ADMINS:
        await message.answer('HEllo brat')

    else:
        await message.answer('Assalomu aleykum Sof gilam yuvish markazining botiga xush kelibsiz',
                             reply_markup=user_menu_keyboard)


@dp.message_handler(text="Kvitansiya raqamini olish 📑")
async def kvitansiya(message: types.Message):
    await message.answer("Telefon raqamingizni yuboring 📱 \n\n(Ma'lumot to'ldirganda bergan raqamingizni kiriting ❗)")
