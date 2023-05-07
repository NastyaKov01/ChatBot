from enum import Enum
from aiogram import types
from aiogram import Dispatcher
import surrogates
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from common import Person, Gender, Activities, generate_recommendation


class BotStates(StatesGroup):
    start_state = State()
    waiting_person = State()
    waiting_gender = State()
    waiting_age = State()
    waiting_activities = State()
    show_result = State()


async def process_start(message: types.Message):
    await message.reply(text='Привет!' + surrogates.decode('\ud83d\ude0a') +
                             'Я бот-помощник.\nПомогу с выбором подарка на день рождения!'
                             + surrogates.decode('\ud83c\udf89'))
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
    answer = 'Введите, пожалуйста, возраст именинни'
    if gender == Gender.MALE:
        answer += 'ка.'
    else:
        answer += 'цы.'
    await message.answer(answer, reply_markup=types.ReplyKeyboardRemove())
    await BotStates.waiting_age.set()


async def process_person_age(message: types.Message, state: FSMContext):
    age = int(message.text)
    ending = ''
    async with state.proxy() as person_info:
        person_info['age'] = age
        if person_info['gender'] == Gender.MALE:
            ending += 'ка'
        else:
            ending += 'цы'
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [act for act in Activities]
    keyboard.add(*buttons)
    answer = f"Выберите, пожалуйста, увлечения именинни{ending} (если мало знаете о них, нажмите на 'мы мало знакомы')." + \
             "\nЧтобы закончить ввод, отправьте сообщение 'все', 'всё' или 'stop'."
    await message.answer(answer, reply_markup=keyboard)
    await BotStates.waiting_activities.set()


async def process_person_activities(message: types.Message, state: FSMContext):
    activity = message.text
    if activity in ('stop', 'все', 'всё'):
        await message.answer('Вот, что я могу порекомендовать!' + surrogates.decode('\u2728'),
                             reply_markup=types.ReplyKeyboardRemove())
        async with state.proxy() as person_info:
            print(person_info)
            answer = generate_recommendation(person_info=person_info)
        print(answer)
        await message.answer(answer)
        await BotStates.start_state.set()
    elif activity in list(Activities):
        async with state.proxy() as person_info:
            if 'activities' not in person_info:
                person_info['activities'] = {activity}
            else:
                person_info['activities'].add(activity)


async def show_result(message: types.Message, state: FSMContext):
    async with state.proxy() as person_info:
        print(person_info)
        answer = generate_recommendation(person_info=person_info)
    await message.answer(answer)
    await BotStates.start_state.set()


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(process_start, commands=['start'], state='*')
    dp.register_message_handler(process_person_type, state=BotStates.waiting_person)
    dp.register_message_handler(process_person_gender, state=BotStates.waiting_gender)
    dp.register_message_handler(process_person_age, state=BotStates.waiting_age)
    dp.register_message_handler(process_person_activities, state=BotStates.waiting_activities)
    dp.register_message_handler(show_result, state=BotStates.show_result)
