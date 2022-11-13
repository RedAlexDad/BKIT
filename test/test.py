# Подключаем библиотеку unitetest для тестирования
import unittest

'''
assertEqual(self, first, second)
first - передаваемое значение
second - полученное значение (в тело функции должен быть return, если вы там не оставили, тогда прописать здесь как None)
если передаваемое значение совпадает с полученным значением, то тест пройден успешно
'''

from function.summa import summa

# Тест на сумму
class test_sum(unittest.TestCase):
    def test_int(self):
        self.assertEqual(
            summa(1, 2), 3)
        print(f'Сумма двух чисел: {1} и {2} равен {3}'
        )

    def test_float(self):
        self.assertEqual(
            summa(1.5, 5.5), 7
        )
        print(f'Сумма двух чисел: {1.5} и {5.5} равен {7}')

from function.bubble_sort import bubble_sort

# Попробуем создать тест на правильность сортировку массива
class bubble_sort_test(unittest.TestCase):
    # Проверим на сортировку
    def test(self):
        self.assertEqual(
            bubble_sort([7, 3, 5, 1, 8]), [1, 3, 5, 7, 8]
        )

    # Если массив пустой
    def test_empty(self):
        self.assertEqual(
            bubble_sort([]), []
        )

    # Проверка на одного элемента
    def test_signle(self):
        self.assertEqual(
            bubble_sort([1]), [1]
        )


from function.simple_value import simple_value

# Тест на простых чисел
class simple_value_test(unittest.TestCase):
    # Простое число: 1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 27, 31
    def test_simple(self):
        self.assertEqual(
            simple_value(3), "Это число является простым"
        )
        print("Это число является простым")
    # Составное число (не простое число)
    def test_no_simple(self):
        self.assertEqual(
            # simple_value(4), None
            simple_value(4), "Это число не является простым"
        )
        print("Это число не является простым")

    # Нулевое число
    def test_zero(self):
        self.assertEqual(
            # simple_value(4), None
            simple_value(0), "Нулевое число не является простым"
        )
        print("Нулевое число не является простым")

    # Единица
    def test_one(self):
        self.assertEqual(
            # simple_value(4), None
            simple_value(1), "Это число не является ни простым, ни составным числом"
        )
        print("Это число не является ни простым, ни составным числом")


if __name__ == '__main__':
    unittest.main()