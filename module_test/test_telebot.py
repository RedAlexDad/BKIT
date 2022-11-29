import unittest
import os.path

from calculate.work_with_calculate import generate_value


class test_telebot(unittest.TestCase):

    # Проверка создания файла и наличия файла
    def test_create_file_json(self):
        message_from_user_id = 369350478

        generate_value(str(message_from_user_id))

        self.assertEqual(
            os.path.exists('D:\Python\BKIT\calculate\data.json'),
            True
        )
