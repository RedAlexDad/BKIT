import unittest

from calculate.json_function import load_data_all, write_data, merge_data, load_data_for_id_user, delete_data_for_id_user

data_json = {
    "id_user": [
        {
            "id": 12425,
            "value": '30 + 40',
            "result": '70'
        }
    ]
}

data_json_big = {
    "id_user": [
        {
            "id": 52478,
            "value": '10 + 10',
            "result": '20'
        },
        {
            "id": 5437,
            "value": '10 + 10',
            "result": '20'
        },
        {
            "id": 69823,
            "value": '10 + 10',
            "result": '20'
        },
        {
            "id": 24537,
            "value": '10 + 10',
            "result": '20'
        },
        {
            "id": 786,
            "value": '10 + 10',
            "result": '20'
        }
    ]
}

data_json1 = {
    "id_user": [
        {
            "id": 324,
            "value": '50 + 50',
            "result": '100'
        }
    ]
}

data_json_with_id = {
    "369350471": [
        {
            "id": 12425,
            "value": '30 + 40',
            "result": '70'
        }
    ]
}

data_json_with_id_1 = {
    "369350471": [
        {
            "id": 78678,
            "value": '70 + 40',
            "result": '110'
        }
    ]
}

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

class test_json(unittest.TestCase):

    # Проверка на присутствия файла
    def test_write_and_read_file(self):
        # Создаем файл с данным
        write_data(data_json)

        # Проверяем на наличие и сходимости
        self.assertEqual(
            load_data_all(),
            {'id_user': [{'id': 12425, 'result': '70', 'value': '30 + 40'}]}
        )

    # Проверка на добавлении json дата
    def test_append_json_in_json(self):
        # Создаем файл с данным
        write_data(data_json)

        # Изменяем файл - добавление новые данных
        merge_data(data_json1)

        # Проверяем на наличие и сходимости
        self.assertEqual(
            load_data_all(),
            {'id_user': [
                {'id': 12425, 'result': '70', 'value': '30 + 40'},
                {'id': 324, 'result': '100', 'value': '50 + 50'}
            ]})

    # Проверка на добавлении json дата с идентификатором пользователя
    def test_and_read_file_with_id(self):
        # Создаем файл с данным
        write_data(data_json_with_id)

        # Проверяем на наличие и сходимости
        self.assertEqual(
            load_data_all(),
            {'369350471': [{'id': 12425, 'result': '70', 'value': '30 + 40'}]}
        )

    # Проверка на добавлении json дата с идентификатором пользователя
    def test_append_json_in_json_with_id(self):
        # Создаем файл с данным
        write_data(data_json_with_id)

        # Изменяем файл - добавление новые данных
        merge_data(data_json_with_id_1, str(369350471))

        # Проверяем на наличие и сходимости
        self.assertEqual(
            load_data_all(),
            {'369350471': [
                {'id': 12425, 'result': '70', 'value': '30 + 40'},
                {'id': 78678, 'result': '110', 'value': '70 + 40'}
            ]})

    def test_search_id_user_and_get_info(self):
        # Создаем файл с данным
        write_data(data_json_two_users)

        # Проверяем на наличие и сходимости
        self.assertEqual(
            load_data_for_id_user('198498415'),
            [{'id': 8034, 'result': '96.0', 'value': '15 + 81'},
             {'id': 947, 'result': '5882.0', 'value': '988 + 4894'},
             {'id': 6363, 'result': '10.0', 'value': '8 + 2 1'},
             {'id': 6363, 'result': '10.0', 'value': '8 + 2 1'}])


    def test_delete_data_of_id_user(self):
        # Создаем файл с данным
        write_data(data_json_two_users)

        # Удаляем данные по id пользователя
        delete_data_for_id_user('369350478')

        # Проверяем на наличие и сходимости
        self.assertEqual(
            load_data_for_id_user('198498415'),
            [{'id': 8034, 'result': '96.0', 'value': '15 + 81'},
             {'id': 947, 'result': '5882.0', 'value': '988 + 4894'},
             {'id': 6363, 'result': '10.0', 'value': '8 + 2 1'},
             {'id': 6363, 'result': '10.0', 'value': '8 + 2 1'}])
