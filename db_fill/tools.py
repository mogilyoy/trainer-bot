from db import Database
from config import db_uri

db = Database(db_uri=db_uri)

def add_programs_to_db():
    for i in range(1, 15):
        with open(f'men_program/program{i}.txt') as f:
            s = f.read()
            print(i)
            title = s.split('\n')[0]
            db.add_program(title, s)

    for i in range(1, 7):
        with open(f'men_program/program15_{i}.txt') as f:
            s = f.read()
            print(f'15_{i}')
            title = s.split('\n')[0]
            db.add_program(title, s)

    for i in range(19, 27):
        with open(f'men_program/program{i}.txt') as f:
            s = f.read()
            title = s.split('\n')[0]
            print(i)
            db.add_program(title, s)

def add_exercises():
    name = []
    muscles = []
    group = []
    image_href = []
    href_l = []
    advice = []
    with open('excercise_group.txt', 'r') as f:
        a = f.readlines()
        for el in a:
            el = el.split(':')
            name.append(el[0])
            muscles.append(el[1])
            group.append(el[2])

    with open('image_href.txt', 'r') as f:
        a = f.readlines()
        for el in a:
            el = el.split(':')
            image_href.append(''.join(el[1:]))
    
    with open('exercise_href.txt', 'r') as f:
        a = f.readlines()
        for el in a:
            el = el.split(':')
            href_l.append(''.join(el[1:]))

    with open('exercise_advice.txt', 'r') as f:
        a = f.readlines()
        for el in a:
            el = el.split(':')
            advice.append(el[1:])

    for i in range(0, len(name)):
        db.add_exercise(i+1, name[i], group[i], muscles[i], image_href[i], href_l[i], advice[i])
        print(i+1)


s = "'Приседания со штангой' varchar, 'Приседания в тренажере Смита' varchar, 'Приседания со штангой на груди в тренажере Смита' varchar, 'Гак-приседания' varchar, 'Жим ногами' varchar, 'Выпады со штангой' varchar, 'Выпады назад' varchar, 'Вышагивания на платформу' varchar, 'Разгибания ног' varchar, 'Рывок штанги на грудь' varchar, 'Становая тяга на прямых ногах' varchar, 'Румынский подъем' varchar, 'Гиперэкстензия для мышц бедра' varchar, 'Сгибание ног лежа' varchar, 'Сгибания ног стоя' varchar, 'Сгибания ног сидя' varchar, 'Подъемы на носки стоя' varchar, 'Подъемы на носки в тренажере для жимов ногами' varchar, 'Подъемы на носки сидя' varchar, 'Подтягивания на перекладине' varchar, 'Тяга штанги в наклоне' varchar, 'Тяга штанги в наклоне обратным хватом' varchar, 'Тяга Т-штанги' varchar, 'Тяга гантели одной рукой в наклоне' varchar, 'Вертикальная тяга широким хватом' varchar, 'Вертикальная тяга обратным хватом' varchar, 'Горизонтальная тяга в блочном тренажере' varchar, 'Пуловер в блочном тренажере стоя' varchar, 'Становая тяга' varchar, 'Наклоны со штангой на плечах' varchar, 'Обратные разведения в тренажере Peck-Deck' varchar, 'Разведение гантелей в наклоне' varchar, 'Подъем гантелей перед собой' varchar, 'Разведение гантелей стоя' varchar, 'Подъем гантелей над головой через стороны' varchar, 'Жим Арнольда' varchar, 'Жим гантелей сидя' varchar, 'Жим штанги сидя' varchar, 'Жим штанги стоя (армейский жим)' varchar, 'Жим штанги лежа' varchar, 'Жим штанги на скамье с наклоном' varchar, 'Жим штанги на скамье с наклоном вниз' varchar, 'Жим гантелей лежа' varchar, 'Жим гантелей на скамье с наклоном вверх' varchar, 'Жим гантелей на скамье с наклоном вниз' varchar, 'Жим от груди в тренажере сидя' varchar, 'Разведение гантелей лежа' varchar, 'Разведение гантелей на скамье с наклоном вверх' varchar, 'Сведения в тренажере Peck-Deck' varchar, 'Сведение в кроссовере через верхние блоки' varchar, 'Сведение в кроссовере через нижние блоки' varchar, 'Шраги со штангой' varchar, 'Шраги со штангой за спиной' varchar, 'Шраги с гантелями' varchar, 'Тяга штанги к подбородку' varchar, 'Скручивание на римском стуле' varchar, 'Скручивания на скамье с наклоном вниз' varchar, 'Скручивание на коленях в болочном тренажере' varchar, 'Обратные скручивания' varchar, 'Подъемы коленей в висе' varchar, 'Подъемы ног в висе' varchar, 'Косые скручивания' varchar, 'Жим штанги узким хватом лежа' varchar, 'Отжимания от скамьи' varchar, 'Французский жим лежа' varchar, 'Французский жим EZ-штанги сидя' varchar, 'Французский жим в тренажере сидя' varchar, 'Жим к низу в блочном тренажере' varchar, 'Жим книзу одной рукой обратным хватом' varchar, 'Разгибание руки с гантелью из-за головы' varchar, 'Разгибания руки с гантелью в наклоне' varchar, 'Подъем штанги на бицепс стоя' varchar, 'Подъемы гантелей на бицепс стоя' varchar, 'Подъем гантелей на бицепс сидя' varchar, 'Молоток' varchar, 'Подъем EZ-штанги на бицепс в скамье Скотта' varchar, 'Подъем гантелей на бицепс в скамье Скотта' varchar, 'Подъем на бицепс в блочном тренажере стоя' varchar, 'Сгибание рук на бицепс в кроссовере' varchar, 'Концентрированный подъем на бицепс' varchar, 'Подъем штанги на бицепс обратным хватом' varchar, 'Сгибания рук в запястьях' varchar"


