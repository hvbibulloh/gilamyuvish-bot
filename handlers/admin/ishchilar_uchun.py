from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentTypes
from loader import bot, dp
from aiogram.dispatcher.filters.state import State, StatesGroup


class RegisterStates(StatesGroup):
    full_name = State()


@dp.message_handler(text="Ro'yxatga olish 📝")
async def register(message: types.Message):
    await message.answer("Mijoz ism familiyasini kiriting !")
