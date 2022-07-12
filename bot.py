from numpy import count_nonzero
import telebot
from config import bot_token, db_uri
import count
import markup
from markup import ProgramPages, ExercisePages, ExercisePagination
import time
from db import Database
from random import choice

bot = telebot.TeleBot(token=bot_token)
pagination1 = ProgramPages(0, 5)
pagination2 = ExercisePages('', 0, 5)
pagination3 = ExercisePagination(0)
db = Database(db_uri=db_uri)

@bot.message_handler(commands='start')
def start(message):
    bot.send_message(message.chat.id, text=random_motivation(), reply_markup=markup.menu())
    if not db.user_exist(message.from_user.id):
        db.add_user_to_user_score(message.from_user.id)


def random_motivation():
    with open('men_program/voitenko.txt', 'r') as f:
        line = f.readlines()
        return choice(line)


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
    if callback.data == 'next_programs_page':
        pagination1.start += 5
        pagination1.end += 5
        bot.edit_message_text(
                chat_id=callback.from_user.id,
                message_id=callback.message.message_id,
                text=random_motivation(),
                reply_markup=markup.all_programs_menu(pagination1.start, pagination1.end),
            )

    if callback.data == 'previous_program_page':
        pagination1.start -= 5
        pagination1.end -= 5
        bot.edit_message_text(
                chat_id=callback.from_user.id,
                message_id=callback.message.message_id,
                text=random_motivation(),
                reply_markup=markup.all_programs_menu(pagination1.start, pagination1.end),
            )
    if callback.data == 'main_menu':
        bot.edit_message_text(
                chat_id=callback.from_user.id,
                message_id=callback.message.message_id,
                text=random_motivation(),
                reply_markup=markup.menu(),
            )

    if callback.data.startswith('program'):
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


    if callback.data == 'all_exercises':
        bot.edit_message_text(
                chat_id=callback.from_user.id,
                message_id=callback.message.message_id,
                text=random_motivation(),
                reply_markup= markup.muscle_group_menu()
            )


    if callback.data.startswith('musc_'):
        pagination2.current = callback.data[5:]
        bot.edit_message_text(
                chat_id=callback.from_user.id,
                message_id=callback.message.message_id,
                text=random_motivation(),
                reply_markup= markup.exercise_menu(pagination2.current, pagination2.start, pagination2.end)
            )
        

    if callback.data == 'next_exercise_page':
        pagination2.start += 5
        pagination2.end += 5
        bot.edit_message_text(
                        chat_id=callback.from_user.id,
                        message_id=callback.message.message_id,
                        text=random_motivation(),
                        reply_markup= markup.exercise_menu(pagination2.current, pagination2.start, pagination2.end)
                    )

    if callback.data == 'previous_exercise_page':
        pagination2.start -= 5
        pagination2.end -= 5
        bot.edit_message_text(
                        chat_id=callback.from_user.id,
                        message_id=callback.message.message_id,
                        text=random_motivation(),
                        reply_markup= markup.exercise_menu(pagination2.current, pagination2.start, pagination2.end)
                    )

    if callback.data.startswith('back') or callback.data.startswith('feet') or callback.data.startswith('breast') or callback.data.startswith('hands') or callback.data.startswith('trapeze') or callback.data.startswith('delta') or callback.data.startswith('press'):
        group = []
        num = []
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
        
        text2 = f'{name}\nГруппа мышц: {muscles}\n Советы:\n{advice[pagination3.current]}'
        bot.send_photo(
            chat_id=callback.from_user.id,
            photo= image_href,
            caption = text2,
            reply_markup = markup.exercise_description(group, num)     
        )

    if callback.data.startswith('advice_back'):
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
        
        text2 = f'{name}\nГруппа мышц: {muscles}\n Советы:\n{advice[pagination3.current]}'
        bot.edit_message_caption(
            chat_id=callback.from_user.id,
            message_id= callback.message.message_id,
            caption = text2,
            reply_markup = markup.exercise_description(group, num)     
        )

    if callback.data.startswith('advice_forward'):
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
        
        text2 = f'{name}\nГруппа мышц: {muscles}\n Советы:\n{advice[pagination3.current]}\n(Для переключения советов нажмите Вперёд или Назад)'
        bot.edit_message_caption(
            chat_id=callback.from_user.id,
            message_id= callback.message.message_id,
            caption = text2,
            reply_markup = markup.exercise_description(group, num)     
        )
    
    if callback.data == 'hide_exercise':
        bot.delete_message(
            chat_id=callback.from_user.id,
            message_id= callback.message.message_id)

    if callback.data == 'my_result':
        bot.edit_message_text(
                chat_id=callback.from_user.id,
                message_id=callback.message.message_id,
                text=random_motivation(),
                reply_markup= markup.result_menu()
            )

    if callback.data == 'my_progress':
        pass

    if callback.data == 'profile':
        pass

    if callback.data == 'write_result':
        msg = bot.edit_message_text(
                chat_id=callback.from_user.id,
                message_id=callback.message.message_id,
                text='Напишите мне свой разультат в формате: "Упражнение - количество". \nЧтобы посмотреть пример записи и подробную информацию отправьте мне\n/score',
                reply_markup= markup.write_result_menu()
            )
        bot.register_next_step_handler(msg, write_result)
        

def write_result(message):
    text = message.text
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
        bot.send_message(message.chat.id, text= f'Ваш результат успешно записан в группу: {el[1]}\nПроверьте результат в разделе Мой прогресс ', reply_markup=markup.write_result_again())

    else: 
        bot.send_message(message.chat.id, text='Неправильный формат данных!\nЧтобы посмотреть пример записи и подробную информацию отправьте мне\n/score', reply_markup=markup.hide_menu())

    

            

if __name__ == '__main__':
    # while True:
    #     try:
            bot.polling(non_stop=True)
        # except:
        #     time.sleep(0.3)

