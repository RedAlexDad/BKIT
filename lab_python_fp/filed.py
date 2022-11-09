import sys
from convert import *

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

def main():
    print('Задача №1 - field.py')
    mas = ''
    if (len(sys.argv) == 1):
        count_argv = int(input('Введите кол-во желаемых аргументов: '))
        if (count_argv > 0):
            for i in range(0, count_argv + 1):
                # print('{}-ый аргумент'.format(i + 1))
                mas += (get_argv(i, '-ый аргумент: '))
                # print('{}-ый аргумент: {}'.format(i + 1, mas[i]))
                mas += ' '
            print(field(goods, mas))
        else:
            print('Ошибка введения кол-во аргументов!')
    elif (len(sys.argv) > 1):
        for i in range(0, len(sys.argv)):
            # print('{}-ый аргумент'.format(i + 1))
            mas += (get_argv(i, '-ый аргумент: '))
            # print('{}-ый аргумент: {}'.format(i + 1, mas[i]))
            mas += ' '
        print(field(goods, mas))
    else:
        print('Ошибка введения аргументов!')


if __name__ == '__main__':
    main()