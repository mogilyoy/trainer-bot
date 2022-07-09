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
            advice.append(el[1])

    for i in range(30, len(name)):
        db.add_exercise(name[i], group[i], muscles[i], image_href[i], href_l[i], advice[i])
        print(i+1)


    
add_exercises()


