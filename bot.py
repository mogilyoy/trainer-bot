import telebot
from config import bot_token, db_uri
import markup
from markup import ProgramPages, ExercisePages, ExercisePagination
import time
from db import Database

bot = telebot.TeleBot(token=bot_token)
pagination1 = ProgramPages(0, 5)
pagination2 = ExercisePages('', 0, 5)
pagination3 = ExercisePagination(0)
db = Database(db_uri=db_uri)

@bot.message_handler(commands='start')
def start(message):
    bot.send_message(message.chat.id, text='Привет, мужик!', reply_markup=markup.menu())


@bot.callback_query_handler(func=lambda call: True)
def callbacks(callback):
    print(callback.data)
    if callback.data == 'all_programs':
        pagination1.start = 0
        pagination1.end = 5
        bot.edit_message_text(
                chat_id=callback.from_user.id,
                message_id=callback.message.message_id,
                text=f"Вот доступные программы тренировок:",
                reply_markup=markup.all_programs_menu(pagination1.start, pagination1.end),
            )
    if callback.data == 'next_programs_page':
        pagination1.start += 5
        pagination1.end += 5
        bot.edit_message_text(
                chat_id=callback.from_user.id,
                message_id=callback.message.message_id,
                text=f"Вот доступные программы тренировок:",
                reply_markup=markup.all_programs_menu(pagination1.start, pagination1.end),
            )

    if callback.data == 'previous_program_page':
        pagination1.start -= 5
        pagination1.end -= 5
        bot.edit_message_text(
                chat_id=callback.from_user.id,
                message_id=callback.message.message_id,
                text=f"Вот доступные программы тренировок:",
                reply_markup=markup.all_programs_menu(pagination1.start, pagination1.end),
            )
    if callback.data == 'main_menu':
        bot.edit_message_text(
                chat_id=callback.from_user.id,
                message_id=callback.message.message_id,
                text=f"Ты сможешь!",
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
                text='Выберите группу мышц:',
                reply_markup= markup.muscle_group_menu()
            )


    if callback.data.startswith('musc_'):
        pagination2.current = callback.data[5:]
        bot.edit_message_text(
                chat_id=callback.from_user.id,
                message_id=callback.message.message_id,
                text=f'Упражнение на группу мышц {pagination2.current}',
                reply_markup= markup.exercise_menu(pagination2.current, pagination2.start, pagination2.end)
            )
        

    if callback.data == 'next_exercise_page':
        pagination2.start += 5
        pagination2.end += 5
        bot.edit_message_text(
                        chat_id=callback.from_user.id,
                        message_id=callback.message.message_id,
                        text=f'Упражнение на группу мышц {pagination2.current}',
                        reply_markup= markup.exercise_menu(pagination2.current, pagination2.start, pagination2.end)
                    )

    if callback.data == 'previous_exercise_page':
        pagination2.start -= 5
        pagination2.end -= 5
        bot.edit_message_text(
                        chat_id=callback.from_user.id,
                        message_id=callback.message.message_id,
                        text=f'Упражнение на группу мышц {pagination2.current}',
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


    
    
       
    

            

if __name__ == '__main__':
    # while True:
    #     try:
            bot.polling(non_stop=True)
        # except:
        #     time.sleep(0.3)

