import unittest
import os.path

from calculate.work_with_calculate import generate_value, get_info_with_id_user, write_data

data_json_two_users = {
    "369350478": [
        {
            "id": 61419,
            "value": 172,
            "result": 836.0
        },
        {
            "id": 1158,
            "value": "10 / 0",
            "result": "inf"
        },
        {
            "id": 5936,
            "value": "10 + 10",
            "result": "20.0"
        },
        {
            "id": 8329,
            "value": "10 + 10",
            "result": "20.0"
        },
        {
            "id": 5287,
            "value": "10 + 10",
            "result": "20.0"
        }
    ],
    "198498415": [
        {
            "id": 8034,
            "value": "15 + 81",
            "result": "96.0"
        },
        {
            "id": 947,
            "value": "988 + 4894",
            "result": "5882.0"
        },
        {
            "id": 6363,
            "value": "8 + 2 1",
            "result": "10.0"
        }
    ]
}


class test_telebot(unittest.TestCase):

    # Проверка создания файла
    def test_create_file_json(self):
        message_from_user_id = 369350478

        generate_value(str(message_from_user_id))

        self.assertEqual(
            os.path.exists('D:\Python\BKIT\calculate\data.json'),
            True
        )

    # Проверка на получение информации по id
    def test_get_info_with_id_user(self):
        write_data(data_json_two_users)

        message_from_user_id = 369350478

        check_info = get_info_with_id_user(str(message_from_user_id))
        print(check_info)
        self.assertEqual(
            check_info, [{'id': 61419, 'result': 836.0, 'value': 172},
                         {'id': 1158, 'result': 'inf', 'value': '10 / 0'},
                         {'id': 5936, 'result': '20.0', 'value': '10 + 10'},
                         {'id': 8329, 'result': '20.0', 'value': '10 + 10'},
                         {'id': 5287, 'result': '20.0', 'value': '10 + 10'},
                         {'id': 5287, 'result': '20.0', 'value': '10 + 10'}]
        )
