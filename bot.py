import matplotlib.pyplot as plt
import seaborn as sbs
import pandas as pd
import telebot
from config import bot_token, db_uri
import count
import markup
from markup import ProgramPages, ExercisePages, ExercisePagination, ProgresPagination, hide_menu
import time
from db import Database
from random import choice
import traceback
import db_fill.texts as texts

bot = telebot.TeleBot(token=bot_token)
pagination1 = ProgramPages(0, 5)
pagination2 = ExercisePages('', 0, 5)
pagination3 = ExercisePagination(0)
pagination4 = ProgresPagination(0, 5)
db = Database(db_uri=db_uri)

@bot.message_handler(commands='start')
def start(message):
    bot.send_message(message.chat.id, text=random_motivation(), reply_markup=markup.menu())
    if not db.user_exist(message.from_user.id):
        db.add_user_to_user_score(message.from_user.id)
    if not db.user_column_exist(message.from_user.id):
        db.add_user_to_user_column(message.from_user.id)


@bot.message_handler(commands='score')
def score(message):
    bot.send_message(
        chat_id=message.from_user.id,
        text=texts.score,
        reply_markup=markup.hide_menu()
    )



def random_motivation():
    with open('men_program/voitenko.txt', 'r') as f:
        line = f.readlines()
        return choice(line)


def build_graph(column, lst):
    if len(lst) > 30: 
        lst = lst[-30:]
    for i in range(len(lst)):
        lst[i] = int(lst[i])
    df = pd.DataFrame({column: lst, 'count': list(range(1, len(lst)+1))})
    sbs.set_style("whitegrid")
    sbs.lineplot(data = df, x = 'count', y = column, legend='full')
    plt.savefig('images/graph.png')
    plt.clf()    


@bot.callback_query_handler(func=lambda call: True)
def callbacks(callback):
    print(callback.data)
    if callback.data == 'all_programs':
        pagination1.start = 0
        pagination1.end = 5
        bot.edit_message_text(
                chat_id=callback.from_user.id,
                message_id=callback.message.message_id,
                text=random_motivation(),
                reply_markup=markup.all_programs_menu(pagination1.start, pagination1.end),
            )
    elif callback.data == 'next_programs_page':
        pagination1.start += 5
        pagination1.end += 5
        bot.edit_message_text(
                chat_id=callback.from_user.id,
                message_id=callback.message.message_id,
                text=random_motivation(),
                reply_markup=markup.all_programs_menu(pagination1.start, pagination1.end),
            )

    elif callback.data == 'previous_program_page':
        pagination1.start -= 5
        pagination1.end -= 5
        bot.edit_message_text(
                chat_id=callback.from_user.id,
                message_id=callback.message.message_id,
                text=random_motivation(),
                reply_markup=markup.all_programs_menu(pagination1.start, pagination1.end),
            )
    elif callback.data == 'main_menu':
        bot.edit_message_text(
                chat_id=callback.from_user.id,
                message_id=callback.message.message_id,
                text=random_motivation(),
                reply_markup=markup.menu(),
            )

    elif callback.data.startswith('program'):
        a = []
        for i in callback.data:
            if i.isnumeric():
                a.append(i)
        a = int(''.join(a))
        bot.edit_message_text(
                chat_id=callback.from_user.id,
                message_id=callback.message.message_id,
                text=db.get_disc(a),
                reply_markup= markup.program_menu()
            )


    elif callback.data == 'all_exercises':
        bot.edit_message_text(
                chat_id=callback.from_user.id,
                message_id=callback.message.message_id,
                text=random_motivation(),
                reply_markup= markup.muscle_group_menu()
            )


    elif callback.data.startswith('musc_'):
        pagination2.current = callback.data[5:]
        bot.edit_message_text(
                chat_id=callback.from_user.id,
                message_id=callback.message.message_id,
                text=random_motivation(),
                reply_markup= markup.exercise_menu(pagination2.current, pagination2.start, pagination2.end)
            )
        

    elif callback.data == 'next_exercise_page':
        pagination2.start += 5
        pagination2.end += 5
        bot.edit_message_text(
                        chat_id=callback.from_user.id,
                        message_id=callback.message.message_id,
                        text=random_motivation(),
                        reply_markup= markup.exercise_menu(pagination2.current, pagination2.start, pagination2.end)
                    )

    elif callback.data == 'previous_exercise_page':
        pagination2.start -= 5
        pagination2.end -= 5
        bot.edit_message_text(
                        chat_id=callback.from_user.id,
                        message_id=callback.message.message_id,
                        text=random_motivation(),
                        reply_markup= markup.exercise_menu(pagination2.current, pagination2.start, pagination2.end)
                    )

    elif callback.data.startswith('back') or callback.data.startswith('feet') or callback.data.startswith('breast') or callback.data.startswith('hands') or callback.data.startswith('trapeze') or callback.data.startswith('delta') or callback.data.startswith('press'):
        group = []
        num = []
        pagination3.current = 0
        for i in callback.data:
            if i.isnumeric():
                num.append(i)
            else:
                group.append(i)
        num = ''.join(num)
        group = ''.join(group)
        exercise = db.get_exercise_info(group, num)
        name = exercise[0]
        muscles = exercise[2]
        image_href = exercise[3]
        advice = exercise[5][2:-2].split('","')
        
        text2 = f'{name}\n???????????? ????????: {muscles}\n ????????????:\n{advice[pagination3.current]}'
        bot.send_photo(
            chat_id=callback.from_user.id,
            photo= image_href,
            caption = text2,
            reply_markup = markup.exercise_description(group, num)     
        )

    elif callback.data.startswith('advice_back'):
        spl = callback.data.split('_')

        group = spl[2]
        num = spl[3]

        pagination3.current -= 1

        exercise = db.get_exercise_info(group, num)
        name = exercise[0]
        group_name = exercise[1]
        muscles = exercise[2]
        image_href = exercise[3]
        advice = exercise[5][2:-2].split('","')
        
        text2 = f'{name}\n???????????? ????????: {muscles}\n ????????????:\n{advice[pagination3.current]}'
        bot.edit_message_caption(
            chat_id=callback.from_user.id,
            message_id= callback.message.message_id,
            caption = text2,
            reply_markup = markup.exercise_description(group, num)     
        )

    elif callback.data.startswith('advice_forward'):
        spl = callback.data.split('_')
        group = spl[2]
        num = spl[3]

        pagination3.current += 1

        exercise = db.get_exercise_info(group, num)
        name = exercise[0]
        group_name = exercise[1]
        muscles = exercise[2]
        image_href = exercise[3]
        advice = exercise[5][2:-2].split('","')
        
        text2 = f'{name}\n???????????? ????????: {muscles}\n ????????????:\n{advice[pagination3.current]}\n(?????? ???????????????????????? ?????????????? ?????????????? ???????????? ?????? ??????????)'
        bot.edit_message_caption(
            chat_id=callback.from_user.id,
            message_id= callback.message.message_id,
            caption = text2,
            reply_markup = markup.exercise_description(group, num)     
        )
    
    elif callback.data == 'hide_exercise':
        bot.delete_message(
            chat_id=callback.from_user.id,
            message_id= callback.message.message_id)

    elif callback.data == 'my_result':
        bot.edit_message_text(
                chat_id=callback.from_user.id,
                message_id=callback.message.message_id,
                text=random_motivation(),
                reply_markup= markup.result_menu()
            )

    elif callback.data == 'write_result':
        msg = bot.edit_message_text(
                chat_id=callback.from_user.id,
                message_id=callback.message.message_id,
                text='???????????????? ?????? ???????? ?????????????????? ?? ??????????????: "???????????????????? ????????????????????". \n?????????? ???????????????????? ???????????? ???????????? ?? ?????????????????? ???????????????????? ?????????????????? ??????\n/score',
                reply_markup= markup.write_result_menu()
            )
        bot.register_next_step_handler(msg, write_result)

    elif callback.data == 'my_progress':
        bot.edit_message_text(
                chat_id=callback.from_user.id,
                message_id=callback.message.message_id,
                text=random_motivation(),
                reply_markup= markup.progress_menu(callback.from_user.id, pagination4.start, pagination4.end)
            )
    elif callback.data == 'next_progress_page':
        pagination4.start += 5
        pagination4.end += 5

        bot.edit_message_text(
                chat_id=callback.from_user.id,
                message_id=callback.message.message_id,
                text=random_motivation(),
                reply_markup= markup.progress_menu(callback.from_user.id, pagination4.start, pagination4.end))

    elif callback.data == 'previous_progress_page':
        pagination4.start -= 5
        pagination4.end -= 5

        bot.edit_message_text(
                chat_id=callback.from_user.id,
                message_id=callback.message.message_id,
                text=random_motivation(),
                reply_markup= markup.progress_menu(callback.from_user.id, pagination4.start, pagination4.end))

    elif callback.data.startswith('progress'):
        column = ' '.join(callback.data.split('_')[1:])
        graph = db.get_user_score_list(callback.from_user.id, column)
        print(column, graph)
        build_graph(column, graph)
        bot.send_photo( 
            chat_id=callback.from_user.id, 
            photo=open('images/graph.png', 'rb'), 
            caption = f'?????? ?????????????????? ???? {column}', 
            reply_markup=markup.hide_menu()
            )

    elif callback.data == 'profile':
        bot.edit_message_text(
                chat_id=callback.from_user.id,
                message_id=callback.message.message_id,
                text=texts.profile(callback.from_user.first_name, callback.from_user.username, callback.from_user.language_code),
                reply_markup= markup.profile_menu()
        )



def write_result(message):
    text = message.text
    if not text.startswith('/'):
        user = message.from_user.id
        exercise_list = db.get_column_names('user_score')

        quan = []
        exercise_name = []

        for i in text:
            if i.isnumeric():
                quan.append(i)
            else: 
                exercise_name.append(i)
        if quan and exercise_name:
            quan = int(''.join(quan))
            exercise_name = ''.join(exercise_name)
            el = count.find_closest(exercise_name.lower().strip(), exercise_list)
            print(el[1])
            db.add_to_user_score(user, el[1], quan)
            db.add_to_user_columns(user, el[1])
            bot.send_message(message.chat.id, text= f'?????? ?????????????????? ?????????????? ?????????????? ?? ????????????: {el[1]}\n?????????????????? ?????????????????? ?? ?????????????? ?????? ???????????????? ', reply_markup=markup.write_result_again())


        else: 
            bot.send_message(message.chat.id, text='???????????????????????? ???????????? ????????????!\n?????????? ???????????????????? ???????????? ???????????? ?? ?????????????????? ???????????????????? ?????????????????? ??????\n/score', reply_markup=markup.hide_menu())
    else:
        if text == '/score':
            score(message)

def send_exeption(exeption):
    bot.send_message(
        chat_id=-1001750080589,
        text=exeption
        )


if __name__ == '__main__':
    while True:
        try:
            bot.polling(non_stop=True)
        except:
            time.sleep(0.3)
            send_exeption(traceback.format_exc())

