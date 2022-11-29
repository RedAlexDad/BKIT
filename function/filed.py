goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
]

# field(goods, 'title') # должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') # должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}

# items = goods, *args = 'title' => len(args) = 1;
# items = goods, *args = ('title', 'price') => len(args) = 2;

def field(items, *args):
    try:
        # Преобразование в кортеж из строки
        argv = into_tuple_from_str(*args)
        assert len(argv) > 0, 'Ошибка! Отсутствуют аргументы!\nПримечание аргументы не должны быть пустыми!'
        # assert len(args) > 0, 'Ошибка! Отсутствуют аргументы!\nПримечание аргументы не должны быть пустыми!'
        r = [{} for i in range(len(items))]
        for i in range(len(items)):
            for j in items[i]:
                #if j in argv:
                if j in argv:
                    r[i].update({j: items[i][j]})
        return r
    except:
        print('Ошибка! Отсутствует список в качестве переданного аргумента!')

# Преобразование в строку из кортежа
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