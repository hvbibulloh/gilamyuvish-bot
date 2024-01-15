from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import config
from utils.postgresql import Database
from config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)
db = Database(DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT)
