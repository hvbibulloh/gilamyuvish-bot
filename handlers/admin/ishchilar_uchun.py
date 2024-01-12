from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentTypes

from keyboard.admin.admin_keys import admin_exit, ishchilar_keyboard, register_keyboard
from loader import bot, dp
from aiogram.dispatcher.filters.state import State, StatesGroup
import config as cfg


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
            await message.answer("Mijoz telefon raqamini kiriting !", reply_markup=admin_exit)

    except:
        await message.answer("Iltimos text ma'lumot kiriting !", reply_markup=admin_exit)


@dp.message_handler(state=RegisterStates.phone_number, content_types=types.ContentTypes.TEXT)
async def phone_number(message: types.Message, state: FSMContext):
    try:
        if message.text == 'Chiqish':
            await message.answer('Bosh menuga qaytdingiz ! ✅', reply_markup=ishchilar_keyboard)
            await state.finish()

        else:
            async with state.proxy() as data:
                data['phone_number'] = message.text

            await RegisterStates.gilam.set()
            await message.answer("Gilamlar sonini kiriting \n❗(Agar mavjud bo'lmasa <O'tkazib yuborish> ni bosing)",
                                 reply_markup=register_keyboard)

    except:
        await message.answer("Iltimos text ma'lumot kiriting !", reply_markup=admin_exit)


@dp.message_handler(state=RegisterStates.gilam, content_types=types.ContentTypes.TEXT)
async def register_gilam(message: types.Message, state: FSMContext):
    try:
        if message.text == 'Chiqish':
            await message.answer('Bosh menugaq qaytdingiz ! ✅', reply_markup=ishchilar_keyboard)
            await state.finish()

        elif message.text == "O'tkazib yuborish":
            await message.answer("Pardalar sonini kiriting \n❗(Agar mavjud bo'lmasa <O'tkazib yuborish> ni bosing)")
            await RegisterStates.next()

        else:
            async with state.proxy() as data:
                data['gilam'] = message.text

            await RegisterStates.parda.state()
            await message.answer("Pardalar sonini kiriting \n❗(Agar mavjud bo'lmasa <O'tkazib yuborish> ni bosing)",
                                 reply_markup=ishchilar_keyboard)


    except:
        await message.answer("Iltimos text ma'lumot kiriting !", reply_markup=admin_exit)


@dp.message_handler(state=RegisterStates.parda, content_types=types.ContentTypes.TEXT)
async def register_parda(message: types.Message, state: FSMContext):
    try:
        if message.text == 'Chiqish':
            await message.answer('Bosh menugaq qaytdingiz ! ✅', reply_markup=ishchilar_keyboard)
            await state.finish()

        elif message.text == "O'tkazib yuborish":
            await message.answer("Yostiqlar sonini kiriting \n❗(Agar mavjud bo'lmasa <O'tkazib yuborish> ni bosing)")
            await RegisterStates.next()

        else:
            async with state.proxy() as data:
                data['yostiq'] = message.text

            await RegisterStates.yostiq.set()
            await message.answer("Yostiqlar sonini kiriting \n❗(Agar mavjud bo'lmasa <O'tkazib yuborish> ni bosing)",
                                 reply_markup=ishchilar_keyboard)
    except:
        await message.answer("Iltimos text ma'lumot kiriting !", reply_markup=admin_exit)


@dp.message_handler(state=RegisterStates.yostiq, content_types=types.ContentTypes.TEXT)
async def register_yostiq(message: types.Message, state: FSMContext):
    try:
        if message.text == 'Chiqish':
            await message.answer('Bosh menugaq qaytdingiz ! ✅', reply_markup=ishchilar_keyboard)
            await state.finish()

        elif message.text == "O'tkazib yuborish":
            await message.answer("Ko'rpalar sonini kiriting \n❗(Agar mavjud bo'lmasa <O'tkazib yuborish> ni bosing)")
            await RegisterStates.next()

        else:
            async with state.proxy() as data:
                data['yostiq'] = message.text

            await RegisterStates.korpa.set()
            await message.answer("Ko'rpalar sonini kiriting \n❗(Agar mavjud bo'lmasa <O'tkazib yuborish> ni bosing)",
                                 reply_markup=ishchilar_keyboard)

    except:
        await message.answer("Iltimos text ma'lumot kiriting !", reply_markup=admin_exit)

@dp.message_handler(state=RegisterStates.korpa, content_types=ContentTypes.TEXT)
async def korpa_text(message: types.Message, state: FSMContext):
    try:
        if message.text == "Chiqish":
            await message.answer('Bosh menugaq qaytdingiz ! ✅', reply_markup=ishchilar_keyboard)
            await state.finish()

        elif message.text == "O'tkazib yuborish":
            await message.answer("Yostiqlar sonini kiriting \n❗(Agar mavjud bo'lmasa <O'tkazib yuborish> ni bosing)")
            await RegisterStates.next()
        else:
            async with state.proxy() as data:
                data['yostiq'] = message.text


