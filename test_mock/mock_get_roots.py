import unittest
import math

# Подключение библиотеки test_mock текст
from unittest.mock import patch

from test_mock.get_roots import get_roots

# Тест на сумму
class test_get_roots(unittest.TestCase):

    # https://tutomath.ru/baza-znanij/bikvadratnye-uravneniya.html
    # Пример №1
    # Дискриминат больше 0 и 4 корней
    @patch('test_mock.get_roots.get_roots')
    def test_example_1(self, mock_roots):
        mock_roots.return_value = [math.sqrt(3), -math.sqrt(3), math.sqrt(2), -math.sqrt(2)]

        self.assertEqual(
            get_roots(1, -5, 6),
            mock_roots.return_value
        )

    # Пример №2
    # Дискриминат равен 0 и 2 корня
    @patch('test_mock.get_roots.get_roots')
    def test_example_2(self, mock_roots):
        mock_roots.return_value = [math.sqrt(2), -math.sqrt(2)]

        self.assertEqual(
            get_roots(1, -4, 4),
            mock_roots.return_value
        )

    # Пример №3
    # Дискриминат больше 0 и 3 корней
    @patch('test_mock.get_roots.get_roots')
    def test_example_3(self, mock_roots):
        mock_roots.return_value = [0, 2, -2]

        self.assertEqual(
            get_roots(-4, 16, 0),
            mock_roots.return_value
        )

    # Пример №4
    # Дискриминат равен 0 и 2 корней
    @patch('test_mock.get_roots.get_roots')
    def test_example_4(self, mock_roots):
        mock_roots.return_value = [2.0, -2.0]

        self.assertEqual(
            get_roots(1, 0, -16),
            mock_roots.return_value
        )

    # Пример №5
    # Дискриминат равен 0 и нет корней
    @patch('test_mock.get_roots.get_roots')
    def test_example_5(self, mock_roots):
        mock_roots.return_value = []

        self.assertEqual(
            get_roots(1, 0, 10),
            mock_roots.return_value
        )

    # Пример №6
    # Дискриминат больше 0 и 2 корня
    @patch('test_mock.get_roots.get_roots')
    def test_example_6(self, mock_roots):
        mock_roots.return_value = [3, -3]

        self.assertEqual(
            get_roots(1, -5, -36),
            mock_roots.return_value
        )

    # Пример №7
    # Дискриминат больше 0 и 4 корней
    @patch('test_mock.get_roots.get_roots')
    def test_example_7(self, mock_roots):
        mock_roots.return_value = [2.0, -2.0, 1.0, -1.0]

        self.assertEqual(
            get_roots(1, -5, 4),
            mock_roots.return_value
        )