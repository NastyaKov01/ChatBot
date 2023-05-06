from aiogram import Dispatcher

from handlers import process_start


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(process_start, commands=['start'])
