import sys

def get_argv(index, prompt):
    try:
        # Получение значения из командной строки
        coef_str = sys.argv[index]
        print(index + 1, prompt, coef_str)
    except:
        # Вводим с клавиатуры
        print(index + 1, prompt, end='')
        coef_str = input()
    # По умолчанию строки
    return coef_str

def into_tuple_from_str(str):
    tuple_buff = []
    str_buff = ''
    for i in range(len(str)):
        if (str[i] == ' '):
            tuple_buff.append(str_buff)
            str_buff = ''
        else:
            str_buff += str[i]

    tuple_buff.append(str_buff)

    return tuple_buff

def into_tuple_from_str_in_value(str):
    tuple_buff = []
    str_buff = ''
    for i in range(len(str)):
        if (str[i] == ' '):
            tuple_buff.append(int(str_buff))
            str_buff = ''
        else:
            str_buff += str[i]

    tuple_buff.append(int(str_buff))

    return tuple_buff

def get_argv_value(index, prompt):
    try:
        # Получение значения из командной строки
        coef_str = sys.argv[index]
    except:
        # Вводим с клавиатуры
        print(prompt, end='')
        coef_str = input()
    # Переводим строку в целое число
    coef = int(coef_str)
    return coef