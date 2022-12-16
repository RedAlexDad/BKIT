import unittest
from unittest.mock import patch

def summa(a, b):
    c = a + b
    return c


class simple_test_mock_summa(unittest.TestCase):

    @patch('simple_test.summa')
    def test_summa_1(self, mock_summa):
        mock_summa.return_value = 2
        self.assertEqual(summa(1, 1), 2)


    @patch('simple_test.summa')
    def test_summa_2(self, mock_summa):
        mock_summa.return_value = 0
        self.assertEqual(summa(-10, 10), 0)