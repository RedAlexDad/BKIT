'''
В предыдущих задачах были написаны все требуемые инструменты для работы с данными.
Применим их на реальном примере.

В файле data_light.json содержится фрагмент списка вакансий.

Структура данных представляет собой список словарей с множеством полей:
название работы, место, уровень зарплаты и т.д.

Необходимо реализовать 4 функции - f1, f2, f3, f4.
Каждая функция вызывается, принимая на вход результат работы предыдущей.
За счет декоратора @print_result печатается результат,
а контекстный менеджер cm_timer_1 выводит время работы цепочки функций.

Предполагается, что функции f1, f2, f3 будут реализованы в одну строку.
В реализации функции f4 может быть до 3 строк.

Функция f1 должна вывести отсортированный список профессий без повторений
(строки в разном регистре считать равными).
Сортировка должна игнорировать регистр.
Используйте наработки из предыдущих задач.

Функция f2 должна фильтровать входной массив и возвращать только те элементы,
которые начинаются со слова “программист”.
Для фильтрации используйте функцию filter.

Функция f3 должна модифицировать каждый элемент массива,
добавив строку “с опытом Python”
(все программисты должны быть знакомы с Python).
Пример:
Программист C# с опытом Python.
Для модификации используйте функцию map.

Функция f4 должна сгенерировать для каждой специальности зарплату
от 100 000 до 200 000 рублей и присоединить её к названию специальности.
Пример:
Программист C# с опытом Python, зарплата 137287 руб.
Используйте zip для обработки пары специальность — зарплата.

Шаблон реализации:
'''

import json
# Сделаем другие необходимые импорты
from operator import concat
from lab_python_fp.filed import *
from lab_python_fp.unique import *
from lab_python_fp.sort import *
from lab_python_fp.print_result import *
from lab_python_fp.cm_timer import *
from lab_python_fp.gen_random import *

path = '../data_light.json'

# Необходимо в переменную path сохранить путь к файлу, который был передан при запуске сценария

# Преобразуем в UTF-8 кодировку, иначе программа неправильно прочтет файл
with open(path, 'r', encoding='UTF-8') as f:
    data = json.load(f)
    # print(data)

# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Предполагается, что функции f1, f2, f3 будут реализованы в одну строку
# В реализации функции f4 может быть до 3 строк

@print_result
def f1(arg):
    # Подбираем названия работы, которые не повторяют друг друга, в список
    # info_job_name = Unique([i['job-name'] for i in field(data, 'job-name')], ignore_case=True)
    # Отсортируем
    # info_job_name_sorted = sorted(info_job_name, key=str, reverse = False)
    # return info_job_name.arr.sort()
    # return sorted(info_job_name, key=str, reverse = False)
    # return sorted(list(set([el['job-name'] for el in arg])), key=lambda a: a.lower())
    return list(Unique([i['job-name'] for i in field(data, 'job-name')], ignore_case=True))


@print_result
def f2(arg):
    return list(filter(lambda i: i.startswith('программист'), arg))


@print_result
def f3(arg):
    return list(map(lambda x: concat(x, ' c опытом Python'), arg))


@print_result
def f4(arg):
    return list(zip(arg, ['зарплата ' + str(el) + ' руб.' for el in gen_random(len(arg), 100000, 200000)]))


if __name__ == '__main__':
    with cm_timer_1():
        # ex_1 = f1(data)
        # ex_2 = f2(f1(data))
        # ex_3 = f3(f2(f1(data)))
        ex_4 = (f4(f3(f2(f1(data)))))
        # (f4(f3(f2(f1(data)))))
        print()