from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentTypes

from keyboard.admin.admin_keys import admin_exit, ishchilar_keyboard, register_keyboard, yes_or_no_keyboard
from keyboard.admin.asosiy_button import asosiy_button
from loader import bot, dp, db
from aiogram.dispatcher.filters.state import State, StatesGroup
import config as cfg


class Tekshirish(StatesGroup):
    kvitansiya = State()


@dp.message_handler(text="Tekshirish 🔍")
async def check_out(message: types.Message):
    if message.from_user.id in cfg.ISHCHI:
        await message.answer('Kvitansiya Raqamini kiriting 🛎', reply_markup=admin_exit)
        await Tekshirish.kvitansiya.set()

    else:
        await message.answer('Siz admin emassiz ⛔')


@dp.message_handler(state=Tekshirish.kvitansiya, content_types=types.ContentTypes.TEXT)
async def check_kv(message: types.Message, state: FSMContext):
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
            if message.text.isdigit():
                mijoz_check = db.get_check(int(data['id']))
                zakaz_check = db.get_check_zakaz(int(data['id']))

            if mijoz_check is None:
                await message.answer("Bunday Kvitansiya raqam mavjud emas ")
            else:
                # Mijoz ma'lumotlari
                await message.answer(f"Mijoz Malumotlari!\nID: <b>{mijoz_check[0]}</b>\nIsm: <b>{mijoz_check[1]}</b>\nTelefon: <b>{mijoz_check[2]}</b>\nAddress: <b>{mijoz_check[7]}</b>\n\n")

                if zakaz_check:
                    await message.answer("<b>Mijozning zakazlari!</b>")
                    print(zakaz_check)
                    for zakaz in zakaz_check:
                        await message.answer(f"Zakaz: {zakaz}")
                else:
                    await message.answer("Mijozning zakazi mavjud emas")

            await message.answer('Tekshirish', reply_markup=ishchilar_keyboard)
            await state.finish()
    except Exception as e:
        print(f"Xatolik: {e}")
        await message.answer("Xatolik yuz berdi, ma'lumotlar saqlanmadi ⚠️", reply_markup=ishchilar_keyboard)
        await state.finish()
