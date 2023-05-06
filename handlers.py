from aiogram import types


async def process_start(message: types.Message):
    print("HELLO")
    await message.reply('Привет! Я бот-помощник при выборе подарка на день рождения!')
