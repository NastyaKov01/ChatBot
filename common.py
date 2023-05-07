from enum import Enum


class Gender(str, Enum):
    MALE = 'Мужской'
    FEMALE = 'Женский'


class Person(str, Enum):
    FAMILY = 'Член семьи'
    FRIEND = 'Друг'
    FELLOW = 'Приятель'
    TEACHER = 'Учитель'
    COLLEAGUE = 'Коллега'


class Activities(str, Enum):
    CULTURE = 'культурные мероприятия'
    HOME = 'домосед'
    SPORT = 'активный образ жизни и спорт'
    NATURE = 'природа'
    ANIMALS = 'животные'
    READ = 'чтение'
    NEW = 'любит узнавать новое'
    PHOTO = 'увлекается фотографией'
    QUEST = 'игры, квесты, головоломки'
    COOK = 'любит вкусно поесть'
    UNKNOWN = 'мы мало знакомы'


class Presents(dict, Enum):
    THEATRE = {
        'name': 'Билет в театр',
        'gender': [Gender.MALE, Gender.FEMALE],
        'person': [Person.FAMILY, Person.FRIEND, Person.TEACHER, Person.COLLEAGUE],
        'age': [15, 100],
        'activities': {Activities.CULTURE}
    }
    CINEMA = {
        'name': 'Билет в кино',
        'gender': [Gender.MALE, Gender.FEMALE],
        'person': [Person.FAMILY, Person.FRIEND, Person.FELLOW],
        'age': [12, 100],
        'activities': {Activities.CULTURE}
    }
    EXHIBITION = {
        'name': 'Билет на выставку',
        'gender': [Gender.MALE, Gender.FEMALE],
        'person': [Person.FAMILY, Person.FRIEND, Person.FELLOW, Person.TEACHER, Person.COLLEAGUE],
        'age': [15, 100],
        'activities': {Activities.CULTURE}
    }
    BOOK = {
        'name': 'Книга',
        'gender': [Gender.MALE, Gender.FEMALE],
        'person': [pers for pers in Person],
        'age': [5, 100],
        'activities': {Activities.CULTURE, Activities.READ, Activities.HOME, Activities.UNKNOWN}
    }
    BOARD_GAME = {
        'name': 'Настольные игры',
        'gender': [Gender.MALE, Gender.FEMALE],
        'person': [Person.FAMILY, Person.FRIEND, Person.FELLOW],
        'age': [5, 100],
        'activities': {Activities.HOME, Activities.QUEST}
    }
    VIDEO_GAME = {
        'name': 'Компьютерные игры (и дополнения к ним)',
        'gender': [Gender.MALE, Gender.FEMALE],
        'person': [Person.FAMILY, Person.FRIEND, Person.FELLOW],
        'age': [10, 60],
        'activities': {Activities.HOME, Activities.QUEST}
    }
    BOOK_CERT = {
        'name': 'Сертификат в книжный магазин',
        'gender': [Gender.MALE, Gender.FEMALE],
        'person': [pers for pers in Person],
        'age': [10, 100],
        'activities': {Activities.READ}
    }
    CRAFT_CERT = {
        'name': 'Сертификат на мастер-класс по изготовлению чего-нибудь своими руками (гончарная мастерская, свечи, панно, картины и пр.)',
        'gender': [Gender.MALE, Gender.FEMALE],
        'person': [Person.FAMILY, Person.FRIEND, Person.COLLEAGUE],
        'age': [15, 60],
        'activities': {Activities.NEW}
    }
    COOK_CERT = {
        'name': 'Сертификат на кулинарный мастер-класс',
        'gender': [Gender.MALE, Gender.FEMALE],
        'person': [Person.FAMILY, Person.FRIEND, Person.COLLEAGUE],
        'age': [15, 60],
        'activities': {Activities.NEW, Activities.COOK}
    }
    DEGUSTATION = {
        'name': 'Билет на дегустацию (сыров, вина, шоколада, закусок и пр.)',
        'gender': [Gender.MALE, Gender.FEMALE],
        'person': [Person.FAMILY, Person.FRIEND, Person.COLLEAGUE],
        'age': [18, 100],
        'activities': {Activities.NEW, Activities.COOK}
    }
    PHOTO_SHOOT = {
        'name': 'Фотосессия',
        'gender': [Gender.FEMALE],
        'person': [Person.FAMILY, Person.FRIEND],
        'age': [18, 50],
        'activities': {Activities.PHOTO, Activities.NEW}
    }
    PHOTO_CERT = {
        'name': 'Сертификат на мастер-класс по фотографии',
        'gender': [Gender.MALE, Gender.FEMALE],
        'person': [Person.FAMILY, Person.FRIEND, Person.COLLEAGUE],
        'age': [18, 100],
        'activities': {Activities.PHOTO}
    }
    COSM_SHOP = {
        'name': 'Сертификат в магазин косметики',
        'gender': [Gender.FEMALE],
        'person': [Person.FAMILY, Person.FRIEND, Person.TEACHER, Person.COLLEAGUE],
        'age': [18, 100],
        'activities': {'universal'}
    }
    COSM_CERT = {
        'name': 'Сертификат на мастер-класс по изготовлению косметики/духов',
        'gender': [Gender.FEMALE],
        'person': [Person.FAMILY, Person.FRIEND, Person.COLLEAGUE],
        'age': [18, 100],
        'activities': {'universal', Activities.NEW}
    }
    FASHION_CERT = {
        'name': 'Сертификат в магазин одежды',
        'gender': [Gender.FEMALE],
        'person': [Person.FAMILY, Person.FRIEND],
        'age': [18, 100],
        'activities': {'universal'}
    }
    SPORT_CERT = {
        'name': 'Сертификат на занятие спортом (скалолазание, серфинг, сплав на байдарках, аэротруба, командные игры и пр.)',
        'gender': [Gender.MALE, Gender.FEMALE],
        'person': [Person.FAMILY, Person.FRIEND, Person.TEACHER, Person.COLLEAGUE],
        'age': [18, 50],
        'activities': {Activities.SPORT, Activities.NEW}
    }
    FIGHT_CERT = {
        'name': 'Сертификат на мастер-класс по стрельбе/борьбе',
        'gender': [Gender.MALE],
        'person': [Person.FAMILY, Person.FRIEND, Person.TEACHER, Person.COLLEAGUE],
        'age': [18, 50],
        'activities': {Activities.SPORT, Activities.NEW}
    }
    QUEST = {
        'name': 'Квест',
        'gender': [Gender.MALE, Gender.FEMALE],
        'person': [Person.FAMILY, Person.FRIEND, Person.COLLEAGUE],
        'age': [18, 50],
        'activities': {Activities.QUEST, Activities.NEW}
    }
    VR = {
        'name': 'VR-квест',
        'gender': [Gender.MALE, Gender.FEMALE],
        'person': [Person.FAMILY, Person.FRIEND, Person.COLLEAGUE],
        'age': [18, 50],
        'activities': {Activities.NEW, Activities.QUEST}
    }
    ANIMALS = {
        'name': 'Билет в контактный зоопарк',
        'gender': [Gender.MALE, Gender.FEMALE],
        'person': [Person.FAMILY, Person.FRIEND, Person.TEACHER, Person.COLLEAGUE],
        'age': [10, 100],
        'activities': {Activities.NATURE, Activities.ANIMALS}
    }
    HORSES = {
        'name': 'Конная прогулка',
        'gender': [Gender.MALE, Gender.FEMALE],
        'person': [Person.FAMILY, Person.FRIEND, ],
        'age': [12, 60],
        'activities': {Activities.SPORT, Activities.NATURE, Activities.ANIMALS}
    }
    FLOWERS = {
        'name': 'Букет цветов',
        'gender': [Gender.FEMALE],
        'person': [pers for pers in Person],
        'age': [0, 100],
        'activities': {'universal', Activities.UNKNOWN}
    }
    SWEETS = {
        'name': 'Конфеты',
        'gender': [Gender.MALE, Gender.FEMALE],
        'person': [pers for pers in Person],
        'age': [0, 100],
        'activities': {'universal', Activities.UNKNOWN}
    }
    CAKE = {
        'name': 'Торт',
        'gender': [Gender.MALE, Gender.FEMALE],
        'person': [pers for pers in Person],
        'age': [0, 100],
        'activities': {'universal', Activities.UNKNOWN}
    }


def get_age_str(age: int):
    if age % 10 == 1:
        if age % 100 == 11:
            year = 'лет'
        else:
            year = 'год'
    elif age % 10 in (2, 3, 4):
        if age % 100 in (12, 13, 14):
            year = 'лет'
        else:
            year = 'года'
    else:
        year = 'лет'
    return year


def get_person_type_with_gender(type: str, gender: str):
    person = ''
    if type == Person.COLLEAGUE:
        person = 'коллеги'
    elif type in (Person.TEACHER, Person.FELLOW):
        if gender == Gender.MALE:
            person = type[:-1].lower() + 'я'
        else:
            person = type.lower() + 'ницы'
    elif type == Person.FAMILY:
        if gender == Gender.MALE:
            person = 'именинника'
        else:
            person = 'именинницы'
    elif type == Person.FRIEND:
        if gender == Gender.MALE:
            person = 'друга'
        else:
            person = 'подруги'
    return person


def generate_recommendation(person_info: dict):
    person = get_person_type_with_gender(person_info['type'], person_info['gender'])
    year = get_age_str(person_info['age'])
    template = f"Варианты подарка для {person} на {person_info['age']} {year}:\n"
    presents = ""
    cnt = 1
    for present in list(Presents):
        if person_info['type'] in present['person'] and person_info['gender'] in present['gender']:
            if present['age'][0] <= person_info['age'] <= present['age'][1]:
                person_info['activities'].add('universal')
                if person_info['activities'] & present['activities']:
                    presents += f"{cnt}. {present['name']}\n"
                    cnt += 1
    return template + presents
