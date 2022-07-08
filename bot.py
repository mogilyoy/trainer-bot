import telebot
from config import bot_token
import markup

bot = telebot.TeleBot(token=bot_token)

@bot.callback_query_handler(func=lambda call: True)
def callbacks(callback):
    if callback.data == '':
        pass



