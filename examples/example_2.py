import telebot
from config import *

bot = telebot.TeleBot(token)

my_name = ['Никита', 'Алеша', 'Егор', 'Влад']

@bot.message_handler(content_types=["text"])
def echo(message):
    if message.text in my_name:
        text = 'Ба! Знакомые все лица'
    else:
        text = message.text
    bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)
