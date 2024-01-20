import asyncio
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentTypes

from keyboard.admin.admin_keys import admin_exit, ishchilar_keyboard, register_keyboard
from loader import bot, dp, db
from aiogram.dispatcher.filters.state import State, StatesGroup
import config as cfg
import re


class RegisterStates(StatesGroup):
    full_name = State()
    phone_number = State()
    gilam = State()
    parda = State()
    yostiq = State()
    korpa = State()
    address = State()


@dp.message_handler(text="Ro'yxatga olish 📝")
async def register(message: types.Message):
    if message.from_user.id in cfg.ISHCHI:
        await message.answer("Mijoz ism familiyasini kiriting !", reply_markup=admin_exit)
        await RegisterStates.full_name.set()
    else:
        await message.answer("Siz admin emassiz ⛔")


@dp.message_handler(state=RegisterStates.full_name, content_types=ContentTypes.TEXT)
async def full_name(message: types.Message, state: FSMContext):
    try:
        if message.text == 'Chiqish':
            await message.answer('Bosh menuga qaytdingiz ❗', reply_markup=ishchilar_keyboard)
            await state.finish()

        else:
            async with state.proxy() as data:
                data['full_name'] = message.text

            await RegisterStates.phone_number.set()
            await message.answer("📱 Mijoz telefon raqamini kiriting \n(+998991234567 manashu formatda bo'lsin)!",
                                 reply_markup=admin_exit)

    except:
        await message.answer("Iltimos text ma'lumot kiriting !", reply_markup=admin_exit)


@dp.message_handler(state=RegisterStates.phone_number, content_types=types.ContentTypes.TEXT)
async def phone_numbers(message: types.Message, state: FSMContext):
    try:
        if message.text == 'Chiqish':
            await message.answer('Bosh menuga qaytdingiz ! ✅', reply_markup=ishchilar_keyboard)
            await state.finish()

        else:
            phone_number = message.text.strip()  # Remove leading and trailing spaces

            # Regex pattern for Uzbekistan mobile numbers
            mobile_pattern = re.compile(r'^\+998[0-9]{9}$')

            if not mobile_pattern.match(phone_number):
                raise ValueError("Noto'g'ri telefon raqami formati")

            async with state.proxy() as data:
                data['phone_number'] = phone_number

                await message.answer(
                    "🧺 Gilamlar sonini kiriting \n‼(Agar mavjud bo'lmasa O'tkazib yuborish ni bosing)",
                    reply_markup=register_keyboard, parse_mode=types.ParseMode.HTML)
                await RegisterStates.gilam.set()

    except ValueError as e:
        await message.answer(f"Xato: {str(e)}", reply_markup=admin_exit)
    except:
        await message.answer("Iltimos text ma'lumot kiriting !", reply_markup=admin_exit)


@dp.message_handler(state=RegisterStates.gilam, content_types=types.ContentTypes.TEXT)
async def register_gilam(message: types.Message, state: FSMContext):
    try:
        if message.text == 'Chiqish':
            await message.answer('Bosh menugaq qaytdingiz ! ✅', reply_markup=ishchilar_keyboard)
            await state.finish()

        elif message.text == "O'tkazib yuborish":
            async with state.proxy() as data:
                data['gilam'] = None

            await message.answer(
                "🎏 Pardalar sonini kiriting \n‼(Agar mavjud bo'lmasa O'tkazib yuborish ni bosing)",
                reply_markup=register_keyboard, parse_mode=types.ParseMode.HTML)

            await RegisterStates.next()

        else:
            async with state.proxy() as data:
                data['gilam'] = message.text

            await RegisterStates.parda.set()
            await message.answer(
                "🎏 Pardalar sonini kiriting \n‼(Agar mavjud bo'lmasa O'tkazib yuborish ni bosing)",
                reply_markup=register_keyboard, parse_mode=types.ParseMode.HTML)


    except:
        await message.answer("Iltimos text ma'lumot kiriting !", reply_markup=admin_exit)


@dp.message_handler(state=RegisterStates.parda, content_types=types.ContentTypes.TEXT)
async def register_parda(message: types.Message, state: FSMContext):
    try:
        if message.text == 'Chiqish':
            await message.answer('Bosh menugaq qaytdingiz ! ✅', reply_markup=ishchilar_keyboard)
            await state.finish()

        elif message.text == "O'tkazib yuborish":
            async with state.proxy() as data:
                data['parda'] = None
            await message.answer(
                "🛏 Yostiqlar sonini kiriting \n‼(Agar mavjud bo'lmasa O'tkazib yuborish ni bosing)",
                reply_markup=register_keyboard, parse_mode=types.ParseMode.HTML)
            await RegisterStates.next()

        else:
            async with state.proxy() as data:
                data['parda'] = message.text

            await RegisterStates.yostiq.set()
            await message.answer(
                "🛏 Yostiqlar sonini kiriting \n‼(Agar mavjud bo'lmasa O'tkazib yuborish ni bosing)",
                reply_markup=register_keyboard, parse_mode=types.ParseMode.HTML)
    except:
        await message.answer("Iltimos text ma'lumot kiriting !", reply_markup=admin_exit)


@dp.message_handler(state=RegisterStates.yostiq, content_types=types.ContentTypes.TEXT)
async def register_yostiq(message: types.Message, state: FSMContext):
    try:
        if message.text == 'Chiqish':
            await message.answer('Bosh menuga qaytdingiz ! ✅', reply_markup=ishchilar_keyboard)
            await state.finish()

        elif message.text == "O'tkazib yuborish":
            async with state.proxy() as data:
                data['yostiq'] = None
            await message.answer(
                "🛌 Ko'rpalar sonini kiriting \n‼(Agar mavjud bo'lmasa O'tkazib yuborish ni bosing)",
                reply_markup=register_keyboard, parse_mode=types.ParseMode.HTML)
            await RegisterStates.next()

        else:
            async with state.proxy() as data:
                data['yostiq'] = message.text

            await RegisterStates.korpa.set()
            await message.answer(
                "🛌 Ko'rpalar sonini kiriting \n‼(Agar mavjud bo'lmasa O'tkazib yuborish ni bosing)",
                reply_markup=register_keyboard, parse_mode=types.ParseMode.HTML)

    except:
        await message.answer("Iltimos text ma'lumot kiriting !", reply_markup=admin_exit)


@dp.message_handler(state=RegisterStates.korpa, content_types=ContentTypes.TEXT)
async def korpa_text(message: types.Message, state: FSMContext):
    try:
        if message.text == "Chiqish":
            await message.answer('Bosh menugaq qaytdingiz ! ✅', reply_markup=ishchilar_keyboard)
            await state.finish()

        elif message.text == "O'tkazib yuborish":
            async with state.proxy() as data:
                data['korpa'] = None
            await message.answer("Mijoz manzilini kiriting ", reply_markup=admin_exit)
            await RegisterStates.next()
        else:
            async with state.proxy() as data:
                data['korpa'] = message.text

            await RegisterStates.address.set()
            await message.answer("📍 Mijoz manzilini kiriting ‼", reply_markup=admin_exit)

    except:
        await message.answer("Iltimos text ma'lumot kiriting !", reply_markup=admin_exit)


@dp.message_handler(state=RegisterStates.address, content_types=ContentTypes.TEXT)
async def address(message: types.Message, state: FSMContext):
    try:
        if message.text == "Chiqish":
            await message.answer('Bosh menuga qaytdingiz ✅', reply_markup=register_keyboard)
            await state.finish()

        else:
            async with state.proxy() as data:
                fullname = data['full_name']
                phone_n = data['phone_number']
                gilam = data['gilam']
                parda = data['parda']
                yostiq = data['yostiq']
                korpa = data['korpa']
                addres = message.text

            db.add_mijoz(fullname, phone_n, gilam, parda, yostiq, korpa, addres)
            await message.answer("Malumotlar saqlandi ✅", reply_markup=ishchilar_keyboard)
            await state.finish()

            await asyncio.sleep(2)
            mijoz_id = db.get_mijoz_id(phone_n)
            for i in range(1, int(gilam)+1):
                db.add_zakaz(name=f"Gilam - {i}", mijoz_id=mijoz_id)
            for i in range(1, int(parda)+1):
                db.add_zakaz(name=f"Parda - {i}", mijoz_id=mijoz_id)
            for i in range(1, int(yostiq)+1):
                db.add_zakaz(name=f"Yostiq - {i}", mijoz_id=mijoz_id)
            for i in range(1, int(korpa)+1):
                db.add_zakaz(name=f"Korpa - {i}", mijoz_id=mijoz_id)
            await message.answer(f"Sizning Kvitansiya raqamingiz 📌: {mijoz_id}")

    except Exception as e:
        print(f"Xatolik: {e}")
        await message.answer("Xatolik yuz berdi, ma'lumotlar saqlanmadi ⚠️", reply_markup=ishchilar_keyboard)
        await state.finish()
