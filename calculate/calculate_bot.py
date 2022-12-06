import config
import telebot
from telebot import types
import random

from calculate_arifmetic import the_simplest_mathematical_calculator as smc
from json_function import merge_data, delete_data_for_id_user, load_data_for_id_user
from work_with_calculate import generate_value

# Создание бота
bot = telebot.TeleBot(config.token)

HELP = '''
/start - Меню переключателя
/calculate - Калькуляторный бот, способный вычислять простейшие арифметические операции
/get_info - Просмотр историю вычисления с БД
/clean - Очистка история вычисления
/random - Генерация случайных вычислений
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
    btn3 = types.InlineKeyboardButton(text="Очистить историю вычисления", callback_data='btn3')
    btn4 = types.InlineKeyboardButton(text="Рандомные вычисления", callback_data='btn4')
    btn5 = types.InlineKeyboardButton(text="Показать фото МГТУ им. Н.Э. Баумана", callback_data='btn5')
    markup.add(btn1, btn2, btn3, btn4, btn5)
    bot.send_message(message.chat.id,
                     text=f"Привет, {message.from_user.first_name}! Я тестовый бот, выберите действия",
                     reply_markup=markup)


# Функция переключателя
@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback_data(callback):
    # Пользовательский идентификатор
    user_id = str(callback.from_user.id)

    if (callback.data == "btn1"):
        bot.send_message(callback.message.chat.id, 'Калькулятор бот')
        bot.send_message(callback.message.chat.id, 'Напишите в чате вычисления')

        # Пользовательский идентификатор
        user_id = str(callback.from_user.id)

        @bot.message_handler(content_types=["text"])
        def echo(message):
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

        data = load_data_for_id_user(str(user_id))
        if(data == 'Error! There is no such identifier'):
            bot.send_message(callback.message.chat.id, 'База данных отсутствует')
        else:
            for j in range(len(data) - 1):
                id = data[j]['id']
                value = data[j]['value']
                result = data[j]['result']
                print_info = f'id: {id}\n{value} = {result}\n\n'
                bot.send_message(callback.message.chat.id, print_info)

    elif(callback.data == "btn3"):
        bot.send_message(callback.message.chat.id, 'Очистка история вычисления')

        check_error = delete_data_for_id_user(user_id)

        if(check_error != 'Error! There is no such identifier'):
            bot.send_message(callback.message.chat.id, 'Успешно')
        else:
            bot.send_message(callback.message.chat.id, check_error)

    elif(callback.data == "btn4"):
        bot.send_message(callback.message.chat.id, 'Генерация случайных вычислений')
        generate_value(user_id)
        bot.send_message(callback.message.chat.id, 'Успешно')

    elif(callback.data == "btn5"):
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


# Просмотри история вычисления
@bot.message_handler(commands=['get_info'])
def start_get_info(message):
    bot.send_message(message.chat.id, 'История вычисления')

    # Пользовательский идентификатор
    user_id = str(message.from_user.id)

    data = load_data_for_id_user(str(user_id))

    if (data == 'Error! There is no such identifier'):
        bot.send_message(message.chat.id, 'База данных отсутствует')
    else:
        for j in range(len(data) - 1):
            id = data[j]['id']
            value = data[j]['value']
            result = data[j]['result']
            print_info = f'id: {id}\n{value} = {result}\n\n'
            bot.send_message(message.chat.id, print_info)


@bot.message_handler(commands=['photo'])
def url(message):
    img = open('bmstu.jpg', 'rb')
    bot.send_photo(message.chat.id, img)

@bot.message_handler(commands=['random'])
def url(message):
    bot.send_message(message.chat.id, 'Генерация случайных вычислений')
    # Пользовательский идентификатор
    user_id = str(message.from_user.id)

    generate_value(user_id)

    bot.send_message(message.chat.id, 'Успешно')
@bot.message_handler(commands=['clean'])
def url(message):
    bot.send_message(message.chat.id, 'Очистка история вычисления')

    # Пользовательский идентификатор
    user_id = str(message.from_user.id)

    check_error = delete_data_for_id_user(user_id)

    if (check_error != 'Error! There is no such identifier'):
        bot.send_message(message.chat.id, 'Успешно')
    else:
        bot.send_message(message.chat.id, check_error)


bot.polling(none_stop=True)
