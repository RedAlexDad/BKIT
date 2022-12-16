import unittest
from unittest.mock import patch, Mock
import worker

class test_worker(unittest.TestCase):
    def test_can_repeat(self):
        sleep_time = 7 * 60 * 60
        expected_result = False

        new_worker = worker.Worker('Bob')

        result = new_worker.can_repeat(sleep_time)

        self.assertEqual(expected_result, result)

    def test_can_repeat_cases(self):
        test_cases = [
            {
                'arguments': {'sleep_time': 9 * 60 * 60},
                'expected_result': True
            },
            {
                'arguments': {'sleep_time': 7 * 60 * 60},
                'expected_result': False
            }
        ]

        new_worker = worker.Worker('Alice')

        for test_case in test_cases:
            # result = new_worker.can_repeat(sleep_time=9 * 60 * 60)
            result = new_worker.can_repeat(**test_case['arguments'])

            self.assertEqual(test_case['expected_result'], result)

    def test_sleep(self):
        sleep_time = 13 * 60 * 60

        new_worker = worker.Worker('Bob')

        with self.assertRaises(Exception):
            _ = new_worker.sleep(sleep_time)

    def test_work(self):
        new_worker = worker.Worker('Alice')

        result = new_worker.work()

        self.assertEqual('Work is done', result)

    @patch.object(worker.Worker, 'eat')
    def test_work_1(self, mock_eat):
        mock_eat.return_value = True

        new_worker = worker.Worker('Bob')

        result = new_worker.work()

        self.assertEqual('Work is done', result)

        mock_eat.assert_called()
        # mock_eat.assert_not_called() # Выводит ошибку

    @staticmethod
    def food_se(args):
        food_dict = {
            1: 'apple',
            2: 'bread',
            3: 'cheese'
        }
        return food_dict.get(args)

    @patch('worker.time.sleep')
    def test_eat(self, _):
        new_worker = worker.Worker('Rock')

        new_worker.food = Mock(side_effect=self.food_se)

        result = new_worker.eat()

        self.assertEqual('applebreadcheese', result)


if (__name__ == '__main__'):
    unittest.main()