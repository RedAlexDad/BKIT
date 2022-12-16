# Подключаем библиотеку unitetest для тестирования
import unittest
import math

'''
assertEqual(self, first, second)
first - передаваемое значение
second - полученное значение (в тело функции должен быть return, если вы там не оставили, тогда прописать здесь как None)
если передаваемое значение совпадает с полученным значением, то тест пройден успешно
'''

from function.Unique import Unique

class test_unique(unittest.TestCase):
    # Проверка на чисел
    def test_value(self):
        # Дан список с числами
        data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
        # Получаем уникальные значения и сохраним его в переменной
        arr_unique = Unique(data).arr
        # Проверяем
        self.assertEqual(
            arr_unique,
            [1, 2]
        )

    # Проверка на буквы
    def test_letters(self):
        # Дан список с числами
        data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
        # Получаем уникальные значения и сохраним его в переменной
        arr_unique = Unique(data).arr
        # Проверяем
        self.assertEqual(
            arr_unique,
            ['a', 'A', 'b', 'B']
        )

    # Проверка на буквы без чувствительного регистра
    def test_letters_ignore_case(self):
        # Дан список с числами
        data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
        # Получаем уникальные значения и сохраним его в переменной
        arr_unique = Unique(data, ignore_case = True).arr
        # Проверяем
        self.assertEqual(
            arr_unique,
            ['a', 'b']
        )


if __name__ == '__main__':
    unittest.main()