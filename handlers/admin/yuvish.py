from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentTypes

from keyboard.admin.admin_keys import admin_exit, ishchilar_keyboard, register_keyboard
from keyboard.admin.asosiy_button import asosiy_button
from loader import bot, dp, db
from aiogram.dispatcher.filters.state import State, StatesGroup
import config as cfg


class YuvishStates(StatesGroup):
    kvitansiya = State()


@dp.message_handler(text="Yuvish 🚿")
async def yuvish(message: types.Message):
    if message.from_user.id in cfg.ISHCHI:
        await message.answer("Mijoz Kvitansiya raqamini kiriting 📃", reply_markup=admin_exit)
        await YuvishStates.kvitansiya.set()

    else:
        await message.answer("Siz admin emassiz")


@dp.message_handler(state=YuvishStates.kvitansiya, content_types=types.ContentTypes.TEXT)
async def yuvish_kvitansiya(message: types.Message, state: FSMContext):
    try:
        kvitansiya_id = int(message.text)
        kvitansiya = db.get_mijoz(kvitansiya_id)

        if message.text == 'Chiqish':
            await message.answer("Bosh menu", reply_markup=ishchilar_keyboard)
            await state.finish()

        elif kvitansiya is None:
            await message.answer("Bunday Kvitansiya raqam mavjud emas ")

        else:
            await message.answer("Kvitansiya mavjud", reply_markup=asosiy_button(kvitansiya_id))


    except Exception as e:
        await message.answer(f"Xatolik: {e}")
        await state.finish()

