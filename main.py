import os
from dotenv import load_dotenv
from aiogram import Bot
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage


class BotStates(StatesGroup):
    pass


if __name__ == '__main__':
    load_dotenv()
    TOKEN = os.getenv('TOKEN')
    bot = Bot(token=TOKEN)
    dp = Dispatcher(bot, storage=MemoryStorage())
    executor.start_polling(dp)
