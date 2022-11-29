
# Преобразование строкого типа в list
def delete_space_into_list(string):
    new_str = []
    str_value = ''
    for i in string:
        if(i != ' '):
            str_value += i
        else:
            new_str.append(str_value)
            str_value = ''

    new_str.append(str_value)

    return new_str


# Расстановка приоритета операции
def enumeration_sign(list_str):
    count_list = []
    for i in list_str:
        if ('*' == i): count_list.append(i)
        if ('/' == i): count_list.append(i)
        if ('+' == i): count_list.append(i)
        if ('-' == i): count_list.append(i)

    count_list = prioritet(count_list)

    return count_list

# Поддержка функции по расстановку приоритета операции
def prioritet(list_str):
    new_list = []
    size = len(list_str)
    count = 0
    while (size != 0):
        if('*' in list_str or '/' in list_str):
            for i in list_str:
                if(i == '*' or i == '/'):
                    new_list.append(i)
            size -= 1
        if('+' in list_str or '-' in list_str):
            for i in list_str:
                if(i == '+' or i == '-'):
                    new_list.append(i)
            size -= 1

    return new_list

# Арифметические операции
def arifmetic(sign, list):
    result = None
    if (sign in list):
        for i in range(1, len(list) - 1):
            try:
                if(list[i] == sign):
                    if(sign == '*'): result = float(list[i - 1]) * float(list[i + 1])
                    elif(sign == '/'): result = float(list[i - 1]) / float(list[i + 1])
                    elif (sign == '+'): result = float(list[i - 1]) + float(list[i + 1])
                    elif (sign == '-'): result = float(list[i - 1]) - float(list[i + 1])

                    list[i] = result
                    del list[i - 1: i]
                    del list[i: i + 1]
            except:
                return result

def calculate(value):
    new_list = delete_space_into_list(value)
    list_en = enumeration_sign(new_list)

    for sgin in list_en:
        arifmetic(sgin, new_list)

    print(float(new_list[0]))
    return float(new_list[0])