import telebot
from config import bot_token, db_uri
import markup
from markup import Pages
import time
from db import Database

bot = telebot.TeleBot(token=bot_token)
pagination = Pages(0, 5)
db = Database(db_uri=db_uri)

@bot.message_handler(commands='start')
def start(message):
    bot.send_message(message.chat.id, text='Привет, мужик!', reply_markup=markup.menu())


@bot.callback_query_handler(func=lambda call: True)
def callbacks(callback):
    print(callback.data)
    if callback.data == 'all_programs':
        pagination.start = 0
        pagination.end = 5
        bot.edit_message_text(
                chat_id=callback.from_user.id,
                message_id=callback.message.message_id,
                text=f"Вот доступные программы тренировок:",
                reply_markup=markup.all_programs_menu(pagination.start, pagination.end),
            )
    if callback.data == 'next_programs_page':
        pagination.start += 5
        pagination.end += 5
        bot.edit_message_text(
                chat_id=callback.from_user.id,
                message_id=callback.message.message_id,
                text=f"Вот доступные программы тренировок:",
                reply_markup=markup.all_programs_menu(pagination.start, pagination.end),
            )

    if callback.data == 'previous_program_page':
        pagination.start -= 5
        pagination.end -= 5
        bot.edit_message_text(
                chat_id=callback.from_user.id,
                message_id=callback.message.message_id,
                text=f"Вот доступные программы тренировок:",
                reply_markup=markup.all_programs_menu(pagination.start, pagination.end),
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
                text=db.get_disc(a),
                reply_markup= markup.exercise_menu()
            )

if __name__ == '__main__':
    # while True:
    #     try:
            bot.polling(non_stop=True)
        # except:
        #     time.sleep(0.3)

