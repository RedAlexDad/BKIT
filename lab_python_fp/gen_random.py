# Пример:
# gen_random(5, 1, 3) должен выдать 5 случайных чисел
# в диапазоне от 1 до 3, например 2, 2, 3, 2, 1
# Hint: типовая реализация занимает 2 строки
import random

def gen_random(num_count, begin, end):
    arr = []
    for i in range(0, num_count):
        arr.append(int(random.uniform(begin, end)))
    return arr