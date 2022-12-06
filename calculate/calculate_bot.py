import config
import telebot
from telebot import types
import random

from calculate_arifmetic import the_simplest_mathematical_calculator as smc
from calculate.work_with_calculate import get_info
from json_function import merge_data

# Создание бота
bot = telebot.TeleBot(config.token)

HELP = '''
/start - Меню переключателя
/calculate - Калькуляторный бот, способный вычислять простейшие арифметические операции
/get_info - Просмотр историю вычисления с БД
/photo - Просмотр фото МГТУ им. Н.Э. Баумана
'''


# Справочник
@bot.message_handler(commands=['help'])
def start(message):
    bot.send_message(message.chat.id, HELP)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text="Посчитать", callback_data='btn1')
    btn2 = types.InlineKeyboardButton(text="Посмотреть историю вычисления", callback_data='btn2')
    btn3 = types.InlineKeyboardButton(text="Показать фото МГТУ им. Н.Э. Баумана", callback_data='btn3')
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id,
                     text=f"Привет, {message.from_user.first_name}! Я тестовый бот, выберите действия",
                     reply_markup=markup)


# Функция переключателя
@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback_data(callback):
    if (callback.data == "btn1"):
        bot.send_message(callback.message.chat.id, 'Калькулятор бот')
        bot.send_message(callback.message.chat.id, 'Напишите в чате вычисления')

        @bot.message_handler(content_types=["text"])
        def echo(message):
            # Пользовательский идентификатор
            user_id = str(message.from_user.id)

            value = smc(message.text)
            bot.send_message(message.chat.id, f'Решение: {value.result}')
            data = {
                user_id: [
                    {"id": random.randint(0, 10000),
                     "value": str(message.text),
                     "result": str(value.result)}
                ]
            }
            merge_data(data, str(message.from_user.id))

    elif(callback.data == "btn2"):
        bot.send_message(callback.message.chat.id, 'История вычисления')
        data = get_info()
        for i in data:
            for j in data[i]:
                id = j['id']
                value = j['value']
                result = j['result']
                print_info = f'id: {id}\n{value} = {result}\n\n'
                bot.send_message(callback.message.chat.id, print_info)

    elif(callback.data == "btn3"):
        img = open('bmstu.jpg', 'rb')
        bot.send_photo(callback.message.chat.id, img)
    else:
        bot.send_message(callback.chat.id, 'Нет такой команды. Введите /help')

# Вычисления
@bot.message_handler(commands=['calculate'])
def start_calculate(message):
    bot.send_message(message.chat.id, 'Калькулятор бот')
    bot.send_message(message.chat.id, 'Напишите в чате вычисления')

    # Пользовательский идентификатор
    user_id = str(message.from_user.id)

    @bot.message_handler(content_types=["text"])
    def echo(message):
        value = calculate(message.text)
        bot.send_message(message.chat.id, f'Решение: {value}')
        data = {
            user_id: [
                {"id": random.randint(0, 10000),
                 "value": str(message.text),
                 "result": str(value)}
            ]
        }
        merge_data(data, str(message.from_user.id))


# Просмотри история вычисления
@bot.message_handler(commands=['get_info'])
def start_get_info(message):
    bot.send_message(message.chat.id, 'История вычисления')

    data = get_info()
    if (data == 'Файл отсутствует'):
        bot.send_message(message.chat.id, 'База данных отсутствует')
    else:
        for i in data:
            for j in data[i]:
                id = j['id']
                value = j['value']
                result = j['result']
                print_info = f'id: {id}\n{value} = {result}\n\n'
                bot.send_message(message.chat.id, print_info)


@bot.message_handler(commands=['photo'])
def url(message):
    img = open('bmstu.jpg', 'rb')
    bot.send_photo(message.chat.id, img)



bot.polling(none_stop=True)
