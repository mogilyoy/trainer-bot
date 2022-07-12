from dataclasses import dataclass
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from db import Database
from config import db_uri


@dataclass
class ProgramPages:
    start: int
    end: int

@dataclass
class ExercisePages:
    current: str
    start: int
    end:int

@dataclass
class ExercisePagination:
    current:int


def menu():
    button3 = InlineKeyboardButton("Мои достижения", callback_data="my_result")
    button1 = InlineKeyboardButton("Программы тренировок", callback_data="all_programs")
    button2 = InlineKeyboardButton("Упражнения", callback_data="all_exercises")
    all_buttons = InlineKeyboardMarkup(
        [[button3], [button1], [button2]], row_width=1
    )
    return all_buttons


def all_programs_menu(start, end):
    db = Database(db_uri=db_uri)
    programs = db.get_all_programs_title()
    titles = []
    for el in programs:
        titles.append(el[0].strip())
    buttons = []

    if end >= len(titles):
        end = len(titles) - 1

    if start < 0: 
        start = 0

    for i, el in enumerate(titles):
        buttons.append(InlineKeyboardButton(text=el, callback_data=f'program{i+1}'))

    menu_button = InlineKeyboardButton(text='<<<<<<<<<<<', callback_data='main_menu')

    if start != 0 and end < len(titles) - 1:
        prev_button = InlineKeyboardButton(text='<<Назад', callback_data='previous_program_page')
        next_button = InlineKeyboardButton(text='Вперед>>', callback_data='next_programs_page')
        all_buttons = InlineKeyboardMarkup(
            [[el] for el in buttons[start:end]] + [[prev_button, next_button], [menu_button]], row_width=1
        )
        return all_buttons

    elif start == 0 and end < len(titles) - 1:
        next_button = InlineKeyboardButton(text='Вперед>>', callback_data='next_programs_page')
        all_buttons = InlineKeyboardMarkup(
            [[el] for el in buttons[start:end]] + [[next_button], [menu_button]], row_width=1
        )
        return all_buttons

    elif start != 0 and end == len(titles) - 1:
        prev_button = InlineKeyboardButton(text='<<Назад', callback_data='previous_program_page')
        all_buttons = InlineKeyboardMarkup(
            [[el] for el in buttons[start:end]] + [[prev_button], [menu_button]], row_width=1
        )
        return all_buttons

    
    else:
        print('что то не так')


def program_menu():
    menu_button = InlineKeyboardButton(text='<<<<<', callback_data='all_programs')
    all_buttons = InlineKeyboardMarkup(
            [[menu_button]], row_width=1
        )
    return all_buttons


def muscle_group_menu():
    db = Database(db_uri=db_uri)
    musc = db.get_musc_groups()
    buttons = []
    back = InlineKeyboardButton(text='<<<<<', callback_data=f'main_menu')
    for i, el in enumerate(musc):
        buttons.append(InlineKeyboardButton(text=el, callback_data=f'musc_{el}'))

    all_buttons = InlineKeyboardMarkup(
            [[el] for el in buttons] + [[back]], row_width=1
        )
    return all_buttons


def exercise_menu(musc_group, start, end):
    db = Database(db_uri=db_uri)
    group = db.get_mus_table_name(musc_group)
    exercise = db.get_group_exercises_name(group)
    buttons = []

    if end >= len(exercise):
        end = len(exercise) - 1
    if start < 0: 
        start = 0
    back = InlineKeyboardButton(text='<<<<<', callback_data=f'all_exercises')

    for i, el in enumerate(exercise):
        buttons.append(InlineKeyboardButton(text=el, callback_data=f'{group[:-3]}{i+1}'))

    if len(exercise) <= 5: 
        end = len(exercise)
        all_buttons = InlineKeyboardMarkup(
                [[el] for el in buttons[start: end]] + [[back]], row_width=1
            )
        return all_buttons

    if start != 0 and end < len(exercise) - 1:
        prev_button = InlineKeyboardButton(text='<<Назад', callback_data='previous_exercise_page')
        next_button = InlineKeyboardButton(text='Вперед>>', callback_data='next_exercise_page')

        all_buttons = InlineKeyboardMarkup(
                [[el] for el in buttons[start: end]] + [[prev_button, next_button], [back]], row_width=1
            )
        return all_buttons  

    elif start == 0:
        next_button = InlineKeyboardButton(text='Вперед>>', callback_data='next_exercise_page')

        all_buttons = InlineKeyboardMarkup(
                [[el] for el in buttons[start: end]] + [[next_button], [back]], row_width=1
            )
        return all_buttons

    elif start != 0 and end == len(exercise) - 1:
        prev_button = InlineKeyboardButton(text='<<Назад', callback_data='previous_exercise_page')
        all_buttons = InlineKeyboardMarkup(
                [[el] for el in buttons[start: end]] + [[prev_button], [back]], row_width=1
            )
        return all_buttons  
    
    else:
        print('что то не так')


def exercise_description(group, num):
    button1 = InlineKeyboardButton(text= '<<Назад', callback_data=f'advice_back_{group}_{num}')
    button2 = InlineKeyboardButton(text= 'Вперёд>>', callback_data=f'advice_forward_{group}_{num}')
    button3 = InlineKeyboardButton(text= 'Скрыть', callback_data=f'hide_exercise')
    all_buttons = InlineKeyboardMarkup(
            [[button1, button2], [button3]], row_width=1
        )
    return all_buttons


def result_menu():
    button1 = InlineKeyboardButton(text= 'Профиль', callback_data='profile')
    button2 = InlineKeyboardButton(text= 'Мой прогресс', callback_data='my_progress')
    button3 = InlineKeyboardButton(text= 'Записать результат', callback_data='write_result')
    back = InlineKeyboardButton(text='<<<<<', callback_data=f'main_menu')
    all_buttons = InlineKeyboardMarkup(
            [[button1], [button2], [button3], [back]], row_width=1
        )
    return all_buttons


def write_result_menu():
    back = InlineKeyboardButton(text='<<<<<', callback_data=f'my_result')   
    all_buttons = InlineKeyboardMarkup(
            [[back]], row_width=1
        )
    return all_buttons


def hide_menu():
    button1 = InlineKeyboardButton(text= 'Скрыть', callback_data='hide_exercise')
    all_buttons = InlineKeyboardMarkup(
            [[button1]], row_width=1
        )
    return all_buttons

def write_result_again():
    button1 = InlineKeyboardButton(text= 'Записать ещё', callback_data='write_result')
    back = InlineKeyboardButton(text='<<<<<', callback_data=f'my_result') 
    button2 = InlineKeyboardButton(text= 'Скрыть', callback_data='hide_exercise')
    all_buttons = InlineKeyboardMarkup(
            [[button1], [back], [button2]], row_width=1
        )
    return all_buttons


    


