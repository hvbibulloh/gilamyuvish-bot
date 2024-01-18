from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentTypes

from keyboard.admin.admin_keys import admin_exit, ishchilar_keyboard, register_keyboard, yes_or_no_keyboard
from keyboard.admin.asosiy_button import asosiy_button
from loader import bot, dp, db
from aiogram.dispatcher.filters.state import State, StatesGroup
import config as cfg


class YuvishStates(StatesGroup):
    kvitansiya = State()
    tanlash = State()
    boyi = State()
    eni = State()
    yes = State()


class TayyorGilam(StatesGroup):
    tayyor = State()


@dp.message_handler(text="Gilam Tayyor ✅")
async def tayyor_gilam(message: types.Message):
    if message.from_user.id in cfg.ISHCHI:
        await message.answer('Kvitansiya Raqamini kiriting 🛎', reply_markup=admin_exit)
        await TayyorGilam.tayyor.set()

    else:
        await message.answer('Siz admin emassiz ⛔')


@dp.message_handler(state=TayyorGilam.tayyor, content_types=ContentTypes.TEXT)
async def tayyor_gilam_now(message: types.Message, state: FSMContext):
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

            db.update_mijoz_nomi(int(data['id']), True)

            await message.answer(f"{data['id']} - Kvitansiya raqamli mijozning gilamlari yuvildi ✅",
                                 reply_markup=ishchilar_keyboard)
            await state.finish()


    except Exception as e:
        print(f"Xatolik: {e}")
        await message.answer("Xatolik yuz berdi, ma'lumotlar saqlanmadi ⚠️", reply_markup=ishchilar_keyboard)
        await state.finish()


@dp.message_handler(text="Gilam Yuvish 🚿")
async def yuvish(message: types.Message):
    if message.from_user.id in cfg.ISHCHI:
        await message.answer("Mijoz Kvitansiya raqamini kiriting 📃", reply_markup=admin_exit)
        await YuvishStates.kvitansiya.set()

    else:
        await message.answer("Siz admin emassiz")


@dp.message_handler(state=YuvishStates.kvitansiya, content_types=types.ContentTypes.TEXT)
async def yuvish_kvitansiya(message: types.Message, state: FSMContext):
    try:
        if message.text == 'Chiqish':
            await message.answer("Bosh menu", reply_markup=ishchilar_keyboard)
            await state.finish()
        elif message.text == '/start':
            await message.answer("Bosh Menu ✅", reply_markup=ishchilar_keyboard)
            await state.finish()
        else:
            kvitansiya_id = int(message.text)
            kvitansiya = db.get_mijoz(kvitansiya_id)
            if kvitansiya is None:
                await message.answer("Bunday Kvitansiya raqam mavjud emas ")
            else:
                async with state.proxy() as data:
                    data['id'] = message.text
                await message.answer(f"{message.text} -  kvitansiya maxsulotlari ✅",
                                     reply_markup=asosiy_button(kvitansiya_id))
                await YuvishStates.tanlash.set()
    except ValueError:
        await message.answer("Noto'g'ri raqam kiritdingiz. Raqam kiriting.")
    except Exception as e:
        await message.answer(f"Xatolik: {e}")
        await state.finish()


@dp.message_handler(state=YuvishStates.tanlash, content_types=types.ContentTypes.TEXT)
async def tanlash(message: types.Message, state: FSMContext):
    try:
        if message.text == 'Chiqish':
            await message.answer("Bosh menu ✅", reply_markup=ishchilar_keyboard)
            await state.finish()

        elif message.text == '/start':
            await message.answer("Bosh Menu ✅", reply_markup=ishchilar_keyboard)
            await state.finish()

        else:
            async with state.proxy() as data:
                data['gilam'] = message.text
            await message.answer("Gilam bo'yini kiriting ‼", reply_markup=admin_exit)
            await YuvishStates.boyi.set()

    except:
        await message.answer("Xatolik", reply_markup=ishchilar_keyboard)
        await state.finish()


@dp.message_handler(state=YuvishStates.boyi, content_types=types.ContentTypes.TEXT)
async def boyi(message: types.Message, state: FSMContext):
    try:
        if message.text == 'Chiqish':
            await message.answer("Bosh Menu ✅", reply_markup=ishchilar_keyboard)
            await state.finish()

        elif message.text == '/start':
            await message.answer("Bosh Menu ✅", reply_markup=ishchilar_keyboard)
            await state.finish()

        else:
            async with state.proxy() as data:
                data['boyi'] = message.text

            await message.answer("Gilam enini kiriting ‼", reply_markup=admin_exit)
            await YuvishStates.eni.set()

    except:
        await message.answer("Xatolik", reply_markup=ishchilar_keyboard)
        await state.finish()


@dp.message_handler(state=YuvishStates.eni, content_types=types.ContentTypes.TEXT)
async def eni(message: types.Message, state: FSMContext):
    try:
        if message.text == 'Chiqish':
            await message.answer("Bosh Menu ✅", reply_markup=ishchilar_keyboard)
            await state.finish()

        elif message.text == '/start':
            await message.answer("Bosh Menu ✅", reply_markup=ishchilar_keyboard)
            await state.finish()

        else:
            async with state.proxy() as data:
                nomi = data['gilam']
                eni = message.text
                boyi = data['boyi']
                kvadrati = float(eni) * float(boyi)
                id = data['id']

            db.add_zakaz(nomi, boyi, eni, kvadrati, id)
            await message.answer("Boshqa maxsulotlarni ham qo'shasizmi?", reply_markup=yes_or_no_keyboard)
            await YuvishStates.yes.set()


    except:
        await message.answer("Xatolik", reply_markup=ishchilar_keyboard)
        await state.finish()


@dp.message_handler(state=YuvishStates.yes, content_types=types.ContentTypes.TEXT)
async def yes_or_no(message: types.Message, state: FSMContext):
    try:
        if message.text == 'Ha ✅':
            async with state.proxy() as data:
                await message.answer(f"{data['id']} kvitansiya maxsulotlari ✅",
                                     reply_markup=asosiy_button(int(data['id'])))
            await YuvishStates.tanlash.set()

        elif message.text == "Yo'q ⛔ Boshqa maxsulot kiritmayman":
            await message.answer("Bosh Menuga qaytdingiz ✅", reply_markup=ishchilar_keyboard)
            await state.finish()

        elif message.text == '/start':
            await message.answer("Bosh Menu ✅", reply_markup=ishchilar_keyboard)
            await state.finish()


    except:
        await message.answer("Xatolik", reply_markup=ishchilar_keyboard)
        await state.finish()
