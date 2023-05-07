from enum import Enum
from aiogram import types
from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from common import Person, Gender, Activities, Presents


class BotStates(StatesGroup):
    start_state = State()
    waiting_person = State()
    waiting_gender = State()
    waiting_age = State()
    waiting_activities = State()


# class BirthdayPerson:
#


async def process_start(message: types.Message):
    print("HELLO")
    await message.reply('Привет! Я бот-помощник при выборе подарка на день рождения!')
    answer = "Кому планируете подарить подарок?"
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [pers for pers in Person]
    print(buttons)
    keyboard.add(*buttons)
    await message.answer(answer, reply_markup=keyboard)
    await BotStates.waiting_person.set()


async def process_person_type(message: types.Message, state: FSMContext):
    person_type = message.text
    print(person_type)
    if person_type not in list(Person):
        await message.answer('Неверный тип получателя. Попробуйте снова.')
    else:
        async with state.proxy() as person_info:
            person_info['type'] = person_type
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = [gend for gend in Gender]
        keyboard.add(*buttons)
        await message.answer('Какого пола именинник?', reply_markup=keyboard)
        await BotStates.waiting_gender.set()


async def process_person_gender(message: types.Message, state: FSMContext):
    gender = message.text
    async with state.proxy() as person_info:
        person_info['gender'] = gender
        print(person_info)
    await message.answer('Введите возраст именинника.')
    await BotStates.waiting_age.set()


async def process_person_age(message: types.Message, state: FSMContext):
    age = int(message.text)
    async with state.proxy() as person_info:
        person_info['age'] = age
        print(person_info)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [act for act in Activities]
    keyboard.add(*buttons)
    await message.answer('Выберите увлечения именника.', reply_markup=keyboard)
    await BotStates.waiting_activities.set()


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(process_start, commands=['start'])
    dp.register_message_handler(process_person_type, state=BotStates.waiting_person)
    dp.register_message_handler(process_person_gender, state=BotStates.waiting_gender)
    dp.register_message_handler(process_person_age, state=BotStates.waiting_age)
