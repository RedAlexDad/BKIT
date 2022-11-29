import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def start(message):
    # markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # btn1 = types.KeyboardButton("Посчитать")
    kb = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text="Посчитать", callback_data='btn1')
    kb.add(btn1)
    # btn2 = types.KeyboardButton("Посмотреть историю вычисления")
    # btn3 = types.KeyboardButton("Показать фото МГТУ им. Н.Э. Баумана")
    # markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id,
                     text=f"Привет, {message.from_user.first_name}! Я тестовый бот, выберите действия",
                     reply_markup=kb)


# @bot.message_handler(content_types=['text'])
@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback_data(callback):
    if(callback.data == "btn1"):
        bot.send_message(callback.message.chat.id, 'test test')
    elif(callback.data == "btn2"):
        bot.send_message(callback.message.chat.id, 'test test')
    elif(callback.data == "btn3"):
        bot.send_message(callback.message.chat.id, 'test test')
    else:
        bot.send_message(callback.chat.id, 'Нет такой команды. Введите /help')

# bot.polling(none_stop=True)
bot.polling()