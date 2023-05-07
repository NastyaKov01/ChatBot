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
    HOME = 'оставаться дома'
    SPORT = 'активный образ жизни и спорт'
    NATURE = 'природу'
    ANIMALS = 'животных'
    READ = 'читать'
    NEW = 'узнавать новое'
    PHOTO = 'увлекается фотографией'
    QUEST = 'игры, квесты, головоломки'
    COOK = 'вкусно поесть'
    UNKNOWN = 'я мало знаком с человеком'


class Presents(dict, Enum):
    THEATRE = {
        'name': 'Билет в театр',
        'gender': [Gender.MALE, Gender.FEMALE],
        'person': [Person.FAMILY, Person.FRIEND, Person.TEACHER, Person.COLLEAGUE],
        'age': [15, 100],
        'activities': [Activities.CULTURE]
    }
    CINEMA = {
        'name': 'Билет в кино',
        'gender': [Gender.MALE, Gender.FEMALE],
        'person': [Person.FAMILY, Person.FRIEND, Person.FELLOW],
        'age': [12, 100],
        'activities': [Activities.CULTURE]
    }
    EXHIBITION = {
        'name': 'Билет на выставку',
        'gender': [Gender.MALE, Gender.FEMALE],
        'age': [15, 100],
        'person': [Person.FAMILY, Person.FRIEND, Person.FELLOW, Person.TEACHER, Person.COLLEAGUE]
    }
    BOOK = {
        'name': 'Книга',
        'gender': [Gender.MALE, Gender.FEMALE],
        'person': [pers for pers in Person],
        'age': [5, 100],
        'activities': [Activities.CULTURE, Activities.READ, Activities.HOME, Activities.UNKNOWN]
    }
    BOARD_GAME = {
        'name': 'Настольные игры',
        'gender': [Gender.MALE, Gender.FEMALE],
        'person': [Person.FAMILY, Person.FRIEND, Person.FELLOW],
        'age': [5, 100],
        'activities': [Activities.HOME, Activities.QUEST]
    }
    VIDEO_GAME = {
        'name': 'Компьютерные игры (и дополнения к ним)',
        'gender': [Gender.MALE, Gender.FEMALE],
        'person': [Person.FAMILY, Person.FRIEND, Person.FELLOW],
        'age': [10, 60],
        'activities': [Activities.HOME, Activities.QUEST]
    }
    BOOK_CERT = {
        'name': 'Сертификат в книжный магазин',
        'gender': [Gender.MALE, Gender.FEMALE],
        'person': [pers for pers in Person],
        'age': [10, 100],
        'activities': [Activities.READ]
    }
    CRAFT_CERT = {
        'name': 'Сертификат на мастер-класс по изготовлению чего-нибудь своими руками (гончарная мастерская, свечи, панно, картины и пр.)',
        'gender': [Gender.MALE, Gender.FEMALE],
        'person': [Person.FAMILY, Person.FRIEND, Person.COLLEAGUE],
        'age': [15, 60],
        'activities': [Activities.NEW]
    }
    COOK_CERT = {
        'name': 'Сертификат на кулинарный мастер-класс',
        'gender': [Gender.MALE, Gender.FEMALE],
        'person': [Person.FAMILY, Person.FRIEND, Person.COLLEAGUE],
        'age': [15, 60],
        'activities': [Activities.NEW, Activities.COOK]
    }
    DEGUSTATION = {
        'name': 'Билет на дегустацию (сыров, вина, шоколада, закусок и пр.)',
        'gender': [Gender.MALE, Gender.FEMALE],
        'person': [Person.FAMILY, Person.FRIEND, Person.COLLEAGUE],
        'age': [18, 100],
        'activities': [Activities.NEW, Activities.COOK]
    }
    PHOTO_SHOOT = {
        'name': 'Фотосессия',
        'gender': [Gender.FEMALE],
        'person': [Person.FAMILY, Person.FRIEND],
        'age': [18, 50],
        'activities': [Activities.PHOTO, Activities.NEW]
    }
    PHOTO_CERT = {
        'name': 'Сертификат на мастер-класс по фотографии',
        'gender': [Gender.MALE, Gender.FEMALE],
        'person': [Person.FAMILY, Person.FRIEND, Person.COLLEAGUE],
        'age': [18, 100],
        'activities': [Activities.PHOTO]
    }
    COSM_SHOP = {
        'name': 'Сертификат в магазин косметики',
        'gender': [Gender.FEMALE],
        'person': [Person.FAMILY, Person.FRIEND, Person.TEACHER, Person.COLLEAGUE],
        'age': [18, 100],
        'activities': ['universal']
    }
    COSM_CERT = {
        'name': 'Сертификат на мастер-класс по изготовлению косметики/духов',
        'gender': [Gender.FEMALE],
        'person': [Person.FAMILY, Person.FRIEND, Person.COLLEAGUE],
        'age': [18, 100],
        'activities': ['universal', Activities.NEW]
    }
    FASHION_CERT = {
        'name': 'Сертификат в магазин одежды',
        'gender': [Gender.FEMALE],
        'person': [Person.FAMILY, Person.FRIEND],
        'age': [18, 100],
        'activities': ['universal']
    }
    SPORT_CERT = {
        'name': 'Сертификат на занятие спортом (скалолазание, серфинг, сплав на байдарках, аэротруба, командные игры и пр.)',
        'gender': [Gender.MALE, Gender.FEMALE],
        'person': [Person.FAMILY, Person.FRIEND, Person.TEACHER, Person.COLLEAGUE],
        'age': [18, 50],
        'activities': [Activities.SPORT, Activities.NEW]
    }
    FIGHT_CERT = {
        'name': 'Сертификат на мастер-класс по стрельбе/борьбе',
        'gender': [Gender.MALE],
        'person': [Person.FAMILY, Person.FRIEND, Person.TEACHER, Person.COLLEAGUE],
        'age': [18, 50],
        'activities': [Activities.SPORT, Activities.NEW]
    }
    QUEST = {
        'name': 'Квест',
        'gender': [Gender.MALE, Gender.FEMALE],
        'person': [Person.FAMILY, Person.FRIEND, Person.COLLEAGUE],
        'age': [18, 50],
        'activities': [Activities.QUEST, Activities.NEW]
    }
    VR = {
        'name': 'VR-квест',
        'gender': [Gender.MALE, Gender.FEMALE],
        'person': [Person.FAMILY, Person.FRIEND, Person.COLLEAGUE],
        'age': [18, 50],
        'activities': [Activities.NEW, Activities.QUEST]
    }
    ANIMALS = {
        'name': 'Билет в контактный зоопарк',
        'gender': [Gender.MALE, Gender.FEMALE],
        'person': [Person.FAMILY, Person.FRIEND, Person.TEACHER, Person.COLLEAGUE],
        'age': [10, 100],
        'activities': [Activities.NATURE, Activities.ANIMALS]
    }
    HORSES = {
        'name': 'Конная прогулка',
        'gender': [Gender.MALE, Gender.FEMALE],
        'person': [Person.FAMILY, Person.FRIEND, ],
        'age': [12, 60],
        'activities': [Activities.SPORT, Activities.NATURE, Activities.ANIMALS]
    }
    FLOWERS = {
        'name': 'Букет цветов',
        'gender': [Gender.FEMALE],
        'person': [pers for pers in Person],
        'age': [0, 100],
        'activities': ['universal', Activities.UNKNOWN]
    }
    SWEETS = {
        'name': 'Конфеты',
        'gender': [Gender.MALE, Gender.FEMALE],
        'person': [pers for pers in Person],
        'age': [0, 100],
        'activities': ['universal', Activities.UNKNOWN]
    }
    CAKE = {
        'name': 'Торт',
        'gender': [Gender.MALE, Gender.FEMALE],
        'person': [pers for pers in Person],
        'age': [0, 100],
        'activities': ['universal', Activities.UNKNOWN]
    }
