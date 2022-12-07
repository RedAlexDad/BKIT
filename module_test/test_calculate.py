import unittest

from calculate.calculate_arifmetic import the_simplest_mathematical_calculator as smc

class test_calculate(unittest.TestCase):

    # Проверка на работу
    def test_1(self):
        self.assertEqual(smc('10.0').result, 10.0)

    def test_2(self):
        self.assertEqual(smc('10 + 10').result, 20.0)

    def test_3(self):
        self.assertEqual(smc('2 + 3 * 2').result, 8.0)

    def test_4(self):
        self.assertEqual(smc('2 + 3 + 2').result, 7.0)

    def test_5(self):
        self.assertEqual(smc('2 + 3 - 2').result, 3.0)

    def test_6(self):
        self.assertEqual(smc('5 / 2 * 2').result, 5.0)

    def test_7(self):
        self.assertEqual(smc('100 - 10 + 100').result, 190.0)

    # Деление на 0
    def test_8(self):
        self.assertEqual(smc('1 / 0').result, 'inf')

    # Умножение на 0
    def test_9(self):
        self.assertEqual(smc('1 * 0').result, 0.0)


if __name__ == '__main__':
    unittest.main()
