import unittest

# Подключение библиотеки test_mock текст
from unittest.mock import patch, Mock

from function.Unique import Unique
from function.get_coef_test import get_coef_test_no_cmd

class test_unique(unittest.TestCase):

    # Проверка на чисел
    @patch('function.Unique.Unique')
    def test_value(self, mock_data):
        mock_data.return_value = [1, 2]

        # Дан список с числами
        data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
        # Получаем уникальные значения и сохраним его в переменной
        arr_unique = Unique(data).arr
        # Проверяем
        self.assertEqual(
            arr_unique,
            mock_data.return_value
        )

    # Проверка на чисел
    @patch('function.get_coef_test.get_coef_test_no_cmd')
    # Тест на обычное числа
    def test_value_index_1(self, mock_value):
        mock_value.return_value = 1.0

        self.assertEqual(
            get_coef_test_no_cmd(1, 1),
            mock_value.return_value
        )

    # Тест на нулевое числа
    @patch('function.get_coef_test.get_coef_test_no_cmd')
    def test_value_index_2(self, mock_value):
        mock_value.return_value = 0.0

        self.assertEqual(
            get_coef_test_no_cmd(2, 0),
            mock_value.return_value
        )


