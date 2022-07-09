from dataclasses import dataclass
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from db import Database
from config import db_uri


@dataclass
class Pages:
    start: int
    end: int


def menu():
    button1 = InlineKeyboardButton("Программы тренирвок", callback_data="all_programs")
    button2 = InlineKeyboardButton("Упражнения", callback_data="all_exercises")
    all_buttons = InlineKeyboardMarkup(
        [[button1], [button2]], row_width=1
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

    if start != 0 and end != len(titles) - 1:
        prev_button = InlineKeyboardButton(text='<<Назад', callback_data='previous_program_page')
        next_button = InlineKeyboardButton(text='Вперед>>', callback_data='next_programs_page')
        all_buttons = InlineKeyboardMarkup(
            [[el] for el in buttons[start:end]] + [[prev_button, next_button], [menu_button]], row_width=1
        )
        return all_buttons

    elif start == 0 and end != len(titles) - 1:
        next_button = InlineKeyboardButton(text='Вперед>>', callback_data='next_programs_page')
        # prev_button = InlineKeyboardButton(text='<<Назад', callback_data='previous_program_page')
        all_buttons = InlineKeyboardMarkup(
            [[el] for el in buttons[start:end]] + [[next_button], [menu_button]], row_width=1
        )
        return all_buttons

    elif start != 0 and end == len(titles) - 1:
        # next_button = InlineKeyboardButton(text='Вперед>>', callback_data='next_programs_page')
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


def exercise_menu():
    pass



# all_programs_menu()