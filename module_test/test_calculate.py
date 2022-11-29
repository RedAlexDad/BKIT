import unittest

from calculate.calculate_arifmetic import calculate

class test_calculate(unittest.TestCase):

    # Проверка на работу
    def test_1(self):
        self.assertEqual(calculate('10'), 10.0)

    def test_2(self):
        self.assertEqual(calculate('10 + 10'), 20.0)

    def test_3(self):
        self.assertEqual(calculate('2 + 3 * 2'), 8.0)

    def test_4(self):
        self.assertEqual(calculate('2 + 3 + 2'), 7.0)

    def test_5(self):
        self.assertEqual(calculate('2 + 3 - 2'), 3.0)

    def test_6(self):
        self.assertEqual(calculate('5 / 2 * 2'), 5.0)

    def test_7(self):
        self.assertEqual(calculate('100 - 10 + 100'), 190.0)