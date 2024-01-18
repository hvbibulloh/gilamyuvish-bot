from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentTypes

from keyboard.admin.admin_keys import admin_exit, ishchilar_keyboard, register_keyboard, yes_or_no_keyboard, \
    hammasi_keyboard
from keyboard.admin.asosiy_button import asosiy_button, korpa_button, parda_button, yostiq_button
from loader import bot, dp, db
from aiogram.dispatcher.filters.state import State, StatesGroup
import config as cfg


class KorpaState(StatesGroup):
    kvitansiya = State()
    tanlash = State()
    kg = State()
    yes = State()


class PardaState(StatesGroup):
    kvitansiya = State()
    tanlash = State()
    kg = State()
    yes = State()


class YostiqState(StatesGroup):
    kvitansiya = State()
    tanlash = State()
    kg = State()
    yes = State()


class TayyorHammasi(StatesGroup):
    tayyor = State()


@dp.message_handler(text="Hammasini Yuvish 🚿")
async def boshqa(message: types.Message):
    if message.from_user.id in cfg.ISHCHI:
        await message.answer("Qaysi Birini Yuvamiz 🧽", reply_markup=hammasi_keyboard)
    else:
        await message.answer("Siz admin emassiz")


@dp.message_handler(text="Ko'rpa")
async def korpa_kv(message: types.Message):
    if message.from_user.id in cfg.ISHCHI:
        await message.answer("Mijoz Kvitansiya raqamini kiriting 📌", reply_markup=admin_exit)
        await KorpaState.kvitansiya.set()
    else:
        await message.answer("Siz admin emassiz")


@dp.message_handler(state=KorpaState.kvitansiya, content_types=types.ContentTypes.TEXT)
async def korpa_text(message: types.Message, state: FSMContext):
    try:
        if message.text == 'Chiqish':
            await message.answer("Bosh Menu ✅", reply_markup=ishchilar_keyboard)
            await state.finish()

        elif message.text == '/start':
            await message.answer("Bosh Menu ✅", reply_markup=ishchilar_keyboard)
            await state.finish()

        else:
            kvitansiya_id = int(message.text)
            kvitansiya = db.get_korpa(kvitansiya_id)
            if kvitansiya is None:
                await message.answer("Bunday Kvitansiya mavjud emas ")

            else:
                async with state.proxy() as data:
                    data['id'] = message.text

                await message.answer(f"{message.text} kvitansiya maxsulotlari ✅",
                                     reply_markup=korpa_button(kvitansiya_id))
                await KorpaState.tanlash.set()

    except ValueError:
        await message.answer("Noto'g'ri raqam kiritdingiz. Raqam kiriting.")
    except Exception as e:
        await message.answer(f"Xatolik: {e}")
        await state.finish()


@dp.message_handler(state=KorpaState.tanlash, content_types=types.ContentTypes.TEXT)
async def korpa_tanlash(message: types.Message, state: FSMContext):
    try:
        if message.text == 'Chiqish':
            await message.answer("Bosh menu ✅", reply_markup=ishchilar_keyboard)
            await state.finish()

        elif message.text == '/start':
            await message.answer("Bosh Menu ✅", reply_markup=ishchilar_keyboard)
            await state.finish()

        else:
            async with state.proxy() as data:
                data['korpa'] = message.text

            await message.answer("Ko'rpa Kgsini kiriting !", reply_markup=admin_exit)
            await KorpaState.kg.set()

    except:
        await message.answer("Xatolik", reply_markup=ishchilar_keyboard)
        await state.finish()


@dp.message_handler(state=KorpaState.kg, content_types=types.ContentTypes.TEXT)
async def korpa_kg(message: types.Message, state: FSMContext):
    try:
        if message.text == 'Chiqish':
            await message.answer("Bosh Menu ✅", reply_markup=ishchilar_keyboard)
            await state.finish()

        elif message.text == '/start':
            await message.answer("Bosh Menu ✅", reply_markup=ishchilar_keyboard)
            await state.finish()

        else:
            async with state.proxy() as data:
                nomi = data['korpa']
                boyi = None
                eni = None
                kvadrati = data['kg'] = message.text
                id = data['id']

            db.add_zakaz(nomi, boyi, eni, kvadrati, id)
            await message.answer("Boshqa Maxsulotlarni ham qo'shasizmi?", reply_markup=yes_or_no_keyboard)
            await KorpaState.yes.set()
    except:
        await message.answer("Xatolik", reply_markup=ishchilar_keyboard)
        await state.finish()


@dp.message_handler(state=KorpaState.yes, content_types=types.ContentTypes.TEXT)
async def korpa_yes(message: types.Message, state: FSMContext):
    try:
        if message.text == 'Ha ✅':
            async with state.proxy() as data:
                await message.answer(f"{data['id']} kvitansiya maxsulotlari ✅",
                                     reply_markup=korpa_button(int(data['id'])))

            await KorpaState.tanlash.set()

        elif message.text == "Yo'q ⛔ Boshqa maxsulot kiritmayman":
            await message.answer("Bosh Menuga Qaytdingiz ✅", reply_markup=ishchilar_keyboard)
            await state.finish()

        elif message.text == '/start':
            await message.answer("Bosh Menu ✅", reply_markup=ishchilar_keyboard)
            await state.finish()


    except:
        await message.answer("Xatolik", reply_markup=ishchilar_keyboard)
        await state.finish()


@dp.message_handler(text="Parda")
async def parda_kv(message: types.Message):
    if message.from_user.id in cfg.ISHCHI:
        await message.answer("Mijoz Kvitansiya raqamini kiriting 📌", reply_markup=admin_exit)
        await PardaState.kvitansiya.set()
    else:
        await message.answer("Siz admin emassiz")


@dp.message_handler(state=PardaState.kvitansiya, content_types=types.ContentTypes.TEXT)
async def parda_text(message: types.Message, state: FSMContext):
    try:
        if message.text == 'Chiqish':
            await message.answer("Bosh Menu ✅", reply_markup=ishchilar_keyboard)
            await state.finish()

        elif message.text == '/start':
            await message.answer("Bosh Menu ✅", reply_markup=ishchilar_keyboard)
            await state.finish()

        else:
            kvitansiya_id = int(message.text)
            kvitansiya = db.get_parda(kvitansiya_id)
            if kvitansiya is None:
                await message.answer("Bunday Kvitansiya mavjud emas ")

            else:
                async with state.proxy() as data:
                    data['id'] = message.text

                await message.answer(f"{message.text} kvitansiya maxsulotlari ✅",
                                     reply_markup=parda_button(kvitansiya_id))
                await PardaState.tanlash.set()

    except ValueError:
        await message.answer("Noto'g'ri raqam kiritdingiz. Raqam kiriting.")
    except Exception as e:
        await message.answer(f"Xatolik: {e}")
        await state.finish()


@dp.message_handler(state=PardaState.tanlash, content_types=types.ContentTypes.TEXT)
async def parda_tanlash(message: types.Message, state: FSMContext):
    try:
        if message.text == 'Chiqish':
            await message.answer("Bosh menu ✅", reply_markup=ishchilar_keyboard)
            await state.finish()

        elif message.text == '/start':
            await message.answer("Bosh Menu ✅", reply_markup=ishchilar_keyboard)
            await state.finish()

        else:
            async with state.proxy() as data:
                data['parda'] = message.text

            await message.answer("Parda Kgsini kiriting !", reply_markup=admin_exit)
            await PardaState.kg.set()

    except:
        await message.answer("Xatolik", reply_markup=ishchilar_keyboard)
        await state.finish()


@dp.message_handler(state=PardaState.kg, content_types=types.ContentTypes.TEXT)
async def pardakg(message: types.Message, state: FSMContext):
    try:
        if message.text == 'Chiqish':
            await message.answer("Bosh Menu ✅", reply_markup=ishchilar_keyboard)
            await state.finish()

        elif message.text == '/start':
            await message.answer("Bosh Menu ✅", reply_markup=ishchilar_keyboard)
            await state.finish()

        else:
            async with state.proxy() as data:
                nomi = data['parda']
                boyi = None
                eni = None
                kvadrati = data['kg'] = message.text
                id = data['id']

            db.add_zakaz(nomi, boyi, eni, kvadrati, id)
            await message.answer("Boshqa Maxsulotlarni ham qo'shasizmi?", reply_markup=yes_or_no_keyboard)
            await PardaState.yes.set()
    except:
        await message.answer("Xatolik", reply_markup=ishchilar_keyboard)
        await state.finish()


@dp.message_handler(state=PardaState.yes, content_types=types.ContentTypes.TEXT)
async def korpa_yes(message: types.Message, state: FSMContext):
    try:
        if message.text == 'Ha ✅':
            async with state.proxy() as data:
                await message.answer(f"{data['id']} kvitansiya maxsulotlari ✅",
                                     reply_markup=parda_button(int(data['id'])))

            await PardaState.tanlash.set()

        elif message.text == "Yo'q ⛔ Boshqa maxsulot kiritmayman":
            await message.answer("Bosh Menuga Qaytdingiz ✅", reply_markup=ishchilar_keyboard)
            await state.finish()

        elif message.text == '/start':
            await message.answer("Bosh Menu ✅", reply_markup=ishchilar_keyboard)
            await state.finish()

        elif message.text == 'Chiqish':
            await message.answer("Bosh Menu ✅", reply_markup=ishchilar_keyboard)
            await state.finish()


    except:
        await message.answer("Xatolik", reply_markup=ishchilar_keyboard)
        await state.finish()


@dp.message_handler(text="Yostiq")
async def yostiq_kv(message: types.Message):
    if message.from_user.id in cfg.ISHCHI:
        await message.answer("Mijoz Kvitansiya raqamini kiriting 📌", reply_markup=admin_exit)
        await YostiqState.kvitansiya.set()
    else:
        await message.answer("Siz admin emassiz")


@dp.message_handler(state=YostiqState.kvitansiya, content_types=types.ContentTypes.TEXT)
async def YOSTIQ_text(message: types.Message, state: FSMContext):
    try:
        if message.text == 'Chiqish':
            await message.answer("Bosh Menu ✅", reply_markup=ishchilar_keyboard)
            await state.finish()

        elif message.text == '/start':
            await message.answer("Bosh Menu ✅", reply_markup=ishchilar_keyboard)
            await state.finish()

        else:
            kvitansiya_id = int(message.text)
            kvitansiya = db.get_yostiq(kvitansiya_id)
            if kvitansiya is None:
                await message.answer("Bunday Kvitansiya mavjud emas ")

            else:
                async with state.proxy() as data:
                    data['id'] = message.text

                await message.answer(f"{message.text} kvitansiya maxsulotlari ✅",
                                     reply_markup=yostiq_button(kvitansiya_id))
                await YostiqState.tanlash.set()

    except ValueError:
        await message.answer("Noto'g'ri raqam kiritdingiz. Raqam kiriting.")
    except Exception as e:
        await message.answer(f"Xatolik: {e}")
        await state.finish()


@dp.message_handler(state=YostiqState.tanlash, content_types=types.ContentTypes.TEXT)
async def yostiq_tanlash(message: types.Message, state: FSMContext):
    try:
        if message.text == 'Chiqish':
            await message.answer("Bosh menu ✅", reply_markup=ishchilar_keyboard)
            await state.finish()

        elif message.text == '/start':
            await message.answer("Bosh Menu ✅", reply_markup=ishchilar_keyboard)
            await state.finish()

        else:
            async with state.proxy() as data:
                data['yostiq'] = message.text

            await message.answer("Yostiq Kgsini kiriting !", reply_markup=admin_exit)
            await YostiqState.kg.set()

    except:
        await message.answer("Xatolik", reply_markup=ishchilar_keyboard)
        await state.finish()


@dp.message_handler(state=YostiqState.kg, content_types=types.ContentTypes.TEXT)
async def YOSTIQKG(message: types.Message, state: FSMContext):
    try:
        if message.text == 'Chiqish':
            await message.answer("Bosh Menu ✅", reply_markup=ishchilar_keyboard)
            await state.finish()

        elif message.text == '/start':
            await message.answer("Bosh Menu ✅", reply_markup=ishchilar_keyboard)
            await state.finish()

        else:
            async with state.proxy() as data:
                nomi = data['yostiq']
                boyi = None
                eni = None
                kvadrati = data['kg'] = message.text
                id = data['id']

            db.add_zakaz(nomi, boyi, eni, kvadrati, id)
            await message.answer("Boshqa Maxsulotlarni ham qo'shasizmi?", reply_markup=yes_or_no_keyboard)
            await YostiqState.yes.set()
    except:
        await message.answer("Xatolik", reply_markup=ishchilar_keyboard)
        await state.finish()


@dp.message_handler(state=YostiqState.yes, content_types=types.ContentTypes.TEXT)
async def yostiq_yes(message: types.Message, state: FSMContext):
    try:
        if message.text == 'Ha ✅':
            async with state.proxy() as data:
                await message.answer(f"{data['id']} kvitansiya maxsulotlari ✅",
                                     reply_markup=yostiq_button(int(data['id'])))

            await YostiqState.tanlash.set()

        elif message.text == "Yo'q ⛔ Boshqa maxsulot kiritmayman":
            await message.answer("Bosh Menuga Qaytdingiz ✅", reply_markup=ishchilar_keyboard)
            await state.finish()

        elif message.text == '/start':
            await message.answer("Bosh Menu ✅", reply_markup=ishchilar_keyboard)
            await state.finish()

        elif message.text == 'Chiqish':
            await message.answer("Bosh Menu ✅", reply_markup=ishchilar_keyboard)
            await state.finish()


    except:
        await message.answer("Xatolik", reply_markup=ishchilar_keyboard)
        await state.finish()


@dp.message_handler(text="Hammasi Tayyor ✅")
async def hammasi_tayyor(message: types.Message):
    if message.from_user.id in cfg.ISHCHI:
        await message.answer('Kvitansiya Raqamini kiriting 🛎', reply_markup=admin_exit)
        await TayyorHammasi.tayyor.set()

    else:
        await message.answer('Siz admin emassiz ⛔')


@dp.message_handler(state=TayyorHammasi.tayyor, content_types=types.ContentTypes.TEXT)
async def hammasi_tayyor_now(message: types.Message, state: FSMContext):
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

            db.update_hammasi_tayyor(int(data['id']), True)

            await message.answer(f"{data['id']} - Kvitansiya raqamli mijozning Maxsulotlari yuvildi ✅",
                                 reply_markup=ishchilar_keyboard)
            await state.finish()

    except Exception as e:
        print(f"Xatolik: {e}")
        await message.answer("Xatolik yuz berdi, ma'lumotlar saqlanmadi ⚠️", reply_markup=ishchilar_keyboard)
        await state.finish()
