from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentTypes

from keyboard.admin.admin_keys import admin_exit, ishchilar_keyboard
from loader import bot, dp
from aiogram.dispatcher.filters.state import State, StatesGroup
import config as cfg


class RegisterStates(StatesGroup):
    full_name = State()
    phone_number = State()
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

            await RegisterStates.address.set()
            await message.answer("Mijozning manzilini kiriting !", reply_markup=admin_exit)

    except:
        await message.answer("Iltimos text ma'lumot kiriting !", reply_markup=admin_exit)


@dp.message_handler(state=RegisterStates.address, content_types=types.ContentTypes.TEXT)
async def address(message: types.Message, state: FSMContext):
    try:
        if message.text == 'Chiqish':
            await message.answer('Bosh menuga qaytdingiz ! ✅', reply_markup=ishchilar_keyboard)
            await state.finish()

        else:
            async with state.proxy() as data:
                data['address'] = message.text

            await message.answer("Mijoznin")

    except:
        await message.answer("Iltimos text ma'lumot kiriting !", reply_markup=admin_exit)


