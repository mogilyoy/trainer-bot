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
