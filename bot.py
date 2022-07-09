import telebot
from config import bot_token
import markup
from markup import Pages
import time

bot = telebot.TeleBot(token=bot_token)
pagination = Pages(0, 5)

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


if __name__ == '__main__':
    # while True:
    #     try:
            bot.polling(non_stop=True)
        # except:
        #     time.sleep(0.3)

