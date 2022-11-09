'''Дан массив 1, содержащий положительные и отрицательные числа.
Необходимо одной строкой кода вывести на экран массив 2,
которые содержит значения массива 1,
отсортированные по модулю в порядке убывания.
Сортировку необходимо осуществлять с помощью функции sorted.
Пример:

data = [4, -30, 30, 100, -100, 123, 1, 0, -1, -4]
Вывод: [123, 100, -100, -30, 30, 4, -4, 1, -1, 0]

Необходимо решить задачу двумя способами:

С использованием lambda-функции.
Без использования lambda-функции.
Шаблон реализации:
'''
import sys
from convert import *


data = [4, -30, 100, -100, 123, 1, 0, -1, -4]

def main():
    print(f'Исходный список:\n {data}')

    result_with_lambda = sorted(data, key=lambda i: -abs(i))
    print(f'Отсортированный список с применением lambda-фнукции:\n {result_with_lambda}')

    result = sorted(data, key=abs, reverse=True)
    print(f'Отсортированный список без применении lambda-функции:\n {result}')

    if (len(sys.argv) == 1):
        data_input = into_tuple_from_str_in_value(input('Введите любой символ списка: '))

        print(f'Исходный список:\n {data_input}')

        result_with_lambda = sorted(data_input, key=lambda i: -abs(i))
        print(f'Отсортированный список с применением lambda-фнукции:\n {result_with_lambda}')

        result = sorted(data_input, key=abs, reverse=True)
        print(f'Отсортированный список без применении lambda-функции:\n {result}')

    elif (len(sys.argv) > 1):
        buff = sys.argv[1]
        for i in range(2, len(sys.argv)):
            buff = buff + ' ' + sys.argv[i]

        data_argv = into_tuple_from_str_in_value(buff)

        print(f'Исходный список:\n {data_argv}')

        result_with_lambda = sorted(data_argv, key=lambda i: -abs(i))
        print(f'Отсортированный список с применением lambda-фнукции:\n {result_with_lambda}')

        result = sorted(data_argv, key=abs, reverse=True)
        print(f'Отсортированный список без применении lambda-функции:\n {result}')
    else:
        print('Ошибка введения аргументов!')

if __name__ == '__main__':
    main()