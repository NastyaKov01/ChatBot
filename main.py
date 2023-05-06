import os
import sys
from dotenv import load_dotenv
from aiogram import Bot
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from common import register_handlers


class BotStates(StatesGroup):
    pass


if __name__ == '__main__':
    dotenv_path = os.path.join(os.path.dirname(__file__), 'variables.env')
    print(dotenv_path)
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
    else:
        print("Cannot read env file with token")
        sys.exit()
    TOKEN = os.getenv('TOKEN')
    print(TOKEN)
    bot = Bot(token=TOKEN)
    dispatcher = Dispatcher(bot, storage=MemoryStorage())
    register_handlers(dp=dispatcher)
    executor.start_polling(dispatcher)
