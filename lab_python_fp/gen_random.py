# Пример:
# gen_random(5, 1, 3) должен выдать выдать 5 случайных чисел
# в диапазоне от 1 до 3, например 2, 2, 3, 2, 1
# Hint: типовая реализация занимает 2 строки
import random
import sys
from convert import *

def gen_random(num_count, begin, end):
    arr = []
    # Если начальный диапазон больше конечного, тогда поменяем местами
    if(begin > end): begin, end = end, begin

    for i in range(0, num_count):
        arr.append(int(random.uniform(begin, end)))
    return arr
def main():
    print('Задача №2 - gen_random.py')
    print('Генерация случайных чисел:')
    value = gen_random(get_argv_value(1, 'Введите кол-во: '), get_argv_value(2, 'Введите диапазон от: '),
                       get_argv_value(3, 'Введите диапазон до: '))
    print(value)


if __name__ == '__main__':
    main()