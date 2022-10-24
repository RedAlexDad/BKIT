import sys
from lab_python_fp.filed import *
from lab_python_fp.gen_random import *
from lab_python_fp.unique import *
from lab_python_fp.sort import *


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


def main():
    print("Main")


    '''
    print('Введите номер пункта для выполнения задач')
    print('Задача №1 - field.py')
    print('Задача №2 - gen_random.py')
    print('Задача №3 - unique.py')
    print('Задача №4 - файл sort.py')
    print('Задача №5 - print_result.py')
    print('Задача №6 - print_result.py')
    print('Задача №7 - файл cm_timer.py')

    switch = int(input('Введите номер пункта: '))

    if(switch == 1):
        print('Задача №1 - field.py')
        mas = ''
        if (len(sys.argv) == 1):
            count_argv = int(input('Введите кол-во желаемых аргументов: '))
            if(count_argv > 1):
                for i in range(0, count_argv):
                    # print('{}-ый аргумент'.format(i + 1))
                    mas += (get_argv(i, '-ый аргумент: '))
                    # print('{}-ый аргумент: {}'.format(i + 1, mas[i]))
                    mas += ' '
                print(field(goods, mas))
            else:
                print('Ошибка введения кол-во аргументов!')
        elif(len(sys.argv) > 1):
            for i in range(0, len(sys.argv)):
                # print('{}-ый аргумент'.format(i + 1))
                mas += (get_argv(i, '-ый аргумент: '))
                # print('{}-ый аргумент: {}'.format(i + 1, mas[i]))
                mas += ' '
            print(field(goods, mas))
        else:
            print('Ошибка введения аргументов!')

    elif(switch == 2):
        print('Задача №2 - gen_random.py')
        print('Генерация случайных чисел:')
        gen_random(get_argv_value(1, 'Введите кол-во: '), get_argv_value(2, 'Введите диапазон от: '), get_argv_value(3, 'Введите диапазон до: '))

    elif(switch == 3):
        print('Задача №3 - unique.py')
            data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
            print(data)
            a = Unique(data)
            for i in Unique(a):
                print(i, end=' ')
            print()
        
            data1 = gen_random(10, 1, 3)
            print(data1)
            b = Unique(data1)
            for i in Unique(b):
                print(i, end=' ')
            print()
        
            data2 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
            print(data2)
            c = Unique(data2)
            for i in Unique(c):
                print(i, end=' ')
            print()
            
            d = Unique(data2, ignore_case=True)
             for i in Unique(d):
                print(i, end=' ')
            print()
            
    elif(switch == 4):
        print('Задача №4 - файл sort.py')
        exercise_4_sort()
        
    elif(switch == 5):
        print('Задача №5 - print_result.py')
        
    elif(switch == 6):
        print('Задача №6 - print_result.py')
    elif(switch == 7):
        print('Задача №7 - файл cm_timer.py')
    else:
        print('Нет такого пункта')
    '''


if __name__ == '__main__':
    main()