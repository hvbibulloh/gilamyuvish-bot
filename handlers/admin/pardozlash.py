from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentTypes

from keyboard.admin.admin_keys import admin_exit, ishchilar_keyboard, register_keyboard, yes_or_no_keyboard
from keyboard.admin.asosiy_button import asosiy_button
from loader import bot, dp, db
from aiogram.dispatcher.filters.state import State, StatesGroup
import config as cfg


class PardozlashState(StatesGroup):
    kvitansiya = State()


@dp.message_handler(text="Pardozlash 🧴")
async def pardozlash(message: types.Message):
    if message.from_user.id in cfg.ISHCHI:
        await message.answer(
            "Pardozlangan Kvitansiya Raqamini kiriting 🛎\n\n‼ Diqqat Mijozning maxsuloti to'liq pardozlangan bo'lsagina Kvitansiya kiriting ‼‼",
            reply_markup=admin_exit)
        await PardozlashState.kvitansiya.set()

    else:
        await message.answer('Siz admin emassiz ⛔')


@dp.message_handler(state=PardozlashState.kvitansiya, content_types=ContentTypes.TEXT)
async def pardozlash_text(message: types.Message, state: FSMContext):
    try:
        if message.text == 'Chiqish':
            await message.answer('Bosh menuga Qaytdingiz', reply_markup=ishchilar_keyboard)
            await state.finish()

        elif message.text == '/start':
            await message.answer('Bosh menuga Qaytdingiz', reply_markup=ishchilar_keyboard)
            await state.finish()

        else:
            async with state.proxy() as data:
                data['id'] = message.text

            db.update_pardozlash(int(data['id']), True)
            await message.answer(f"{data['id']} - Kvitansiya raqamli mijozning maxsulotlari pardozlandi ✅",
                                 reply_markup=ishchilar_keyboard)

            await state.finish()

    except Exception as e:
        print(f"Xatolik: {e}")
        await message.answer("Xatolik yuz berdi, ma'lumotlar saqlanmadi ⚠️", reply_markup=ishchilar_keyboard)
        await state.finish()
