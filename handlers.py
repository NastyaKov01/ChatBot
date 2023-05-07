from enum import Enum
from aiogram import types
from aiogram import Dispatcher

from common import Person, Gender, Activities, Presents

# from main import bot


async def process_start(message: types.Message):
    print("HELLO")
    await message.reply('Привет! Я бот-помощник при выборе подарка на день рождения!')
    answer = "Кому планируете подарить подарок?"
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [pers for pers in Person]
    print(buttons)
    keyboard.add(*buttons)
    await message.answer(answer, reply_markup=keyboard)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(process_start, commands=['start'])
