# Подключаем библиотеку unitetest для тестирования
import unittest

'''
assertEqual(self, first, second)
first - передаваемое значение
second - полученное значение (в тело функции должен быть return, если вы там не оставили, тогда прописать здесь как None)
если передаваемое значение совпадает с полученным значением, то тест пройден успешно
'''

from function.filed import field, goods


class test_filed(unittest.TestCase):

    # Проверка вывода с 1 аргумента
    def test_pass_one_argv(self):
        self.assertEqual(
            field(goods, 'title'),
            [
                {'title': 'Ковер'},
                {'title': 'Диван для отдыха'}
            ]
        )

    # Проверка вывода с 2 аргумента
    def test_pass_two_argv(self):
        self.assertEqual(
            field(goods, 'title color'),
            [
                {'color': 'green', 'title': 'Ковер'},
                {'color': 'black', 'title': 'Диван для отдыха'}
            ]
        )

    # Проверка вывода с 3 аргумента
    def test_pass_three_argv(self):
        self.assertEqual(
            field(goods, 'title color price'),
            [
                {'color': 'green', 'price': 2000, 'title': 'Ковер'},
                {'color': 'black', 'price': 5300, 'title': 'Диван для отдыха'}
            ]
        )
