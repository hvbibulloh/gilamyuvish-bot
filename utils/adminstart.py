import logging
from aiogram import Dispatcher
import config


async def on_startup_notify(dp: Dispatcher):
    for admin in config.ADMINS:
        try:
            await dp.bot.send_message(admin, "Bot ishga tushdi 🌙")

        except Exception as err:
            logging.exception(err)
