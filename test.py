import unittest

from RK_2 import Chapter, Book, ChapterBook, exercise_G1, exercies_G2, exercise_G3, books, chapters, chapters_of_books

simple_book = [
    Book(1, 'Азбука'),
    Book(2, 'Программирование на Python'),
    Book(3, 'Математика')
]
simple_chapter = [
    Chapter(1, 'Модульный тест', 10, 2),
    Chapter(2, 'Буква А', 1, 1),
    Chapter(3, 'Плюсик', 4, 3)
]
simple_chapter_of_books = [
    ChapterBook(1, 2),
    ChapterBook(2, 1),
    ChapterBook(3, 3)
]

# Тест на создание класс "Глава"
class test_programms(unittest.TestCase):

    # Класс Chapter с пустыми параметрами
    def test_empty_parametrs_class_chapter(self):
        with self.assertRaises(TypeError) as context:
            # Выводит ошибку, т.к. в классе не было инициализировано по умолчанию
            Chapter()

        self.assertEqual(
            "__init__() missing 4 required positional arguments: 'id', 'name', 'page', " "and 'book_id'",
            str(context.exception))

    # Класс Chapter с пустыми значениями
    def test_empty_class_chapter(self):
        myclass_chapter = Chapter(None, None, None, None)
        self.assertEqual(myclass_chapter.id, None)
        self.assertEqual(myclass_chapter.name, None)
        self.assertEqual(myclass_chapter.page, None)
        self.assertEqual(myclass_chapter.book_id, None)

    # Класс Chapter с значением
    def test_class_chapter(self):
        myclass_chapter = Chapter(1, 'Математическое моделирование', 8, 2)
        self.assertEqual(myclass_chapter.id, 1)
        self.assertEqual(myclass_chapter.name, 'Математическое моделирование')
        self.assertEqual(myclass_chapter.page, 8)
        self.assertEqual(myclass_chapter.book_id, 2)

    # Класс Book с значением
    def test_class_book(self):
        myclass_book = Book(1, 'СХЕМЫ АЛГОРИТМОВ')
        self.assertEqual(myclass_book.id, 1)
        self.assertEqual(myclass_book.name, 'СХЕМЫ АЛГОРИТМОВ')

    # Класс ChapterBook с значением
    def test_class_chapter_book(self):
        myclass_chapter_book = ChapterBook(2, 1)
        self.assertEqual(myclass_chapter_book.book_id, 2)
        self.assertEqual(myclass_chapter_book.chapter_id, 1)

    # Проверка задания Г1
    def test_exercise_G1(self):
        self.assertEqual(dict(exercise_G1(simple_book, simple_chapter)), {'Азбука': ['Буква А']})

    # Проверка задания Г2
    def test_exercise_G2(self):
        self.assertEqual(dict(exercies_G2(simple_book, simple_chapter)), {'Азбука': 1, 'Математика': 4, 'Программирование на Python': 10})

    # Проверка задания Г3
    def test_exercise_G3(self):
        self.assertEqual(exercise_G3(simple_book, simple_chapter), [('Азбука', 'Буква А'), ('Программирование на Python', 'Модульный тест')])


if __name__ == '__main__':
    unittest.main()
