from aiogram.utils import executor
from utils.set_command import set_default_commands
from utils.adminstart import on_startup_notify
from loader import dp
import handlers, keyboard, states, utils


async def startup(dispatcher):
    await set_default_commands(dispatcher)
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=startup, skip_updates=True)
