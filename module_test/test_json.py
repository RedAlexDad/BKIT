import unittest

from calculate.json_function import load_data, write_data, merge_data

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


class test_json(unittest.TestCase):

    # Проверка на присутствия файла
    def test_write_and_read_file(self):
        # Создаем файл с данным
        write_data(data_json)

        # Проверяем на наличие и сходимости
        self.assertEqual(
            load_data(),
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
            load_data(),
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
            load_data(),
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
            load_data(),
            {'369350471': [
                {'id': 12425, 'result': '70', 'value': '30 + 40'},
                {'id': 78678, 'result': '110', 'value': '70 + 40'}
            ]})

