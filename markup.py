from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def menu():
    button1 = InlineKeyboardButton("Новые заказы", callback_data="new_orders")
    button2 = InlineKeyboardButton("Заказы на сборке", callback_data="show_orders_st1")
    button3 = InlineKeyboardButton("Поставки", callback_data="supplies")
    button4 = InlineKeyboardButton("Шк поставки", callback_data="supply_barcode")
    button5 = InlineKeyboardButton("Шк стикеров", callback_data="stickers_barcode")
    all_buttons = InlineKeyboardMarkup(
        [[button1], [button2], [button3], [button4], [button5]], row_width=1
    )
    return all_buttons

