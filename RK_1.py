from operator import itemgetter
'''
Вариант Г.
«Книга» и «Глава» связаны соотношением один-ко-многим. 
Выведите список всех книг, у которых название начинается с буквы «А», и список содержащих в них глав.

«Книга» и «Глава» связаны соотношением один-ко-многим. 
Выведите список книг с максимальной страницы глав в каждой книге, отсортированный по максимальной странице.

«Книга» и «Глава» связаны соотношением многие-ко-многим. 
Выведите список всех связанных глав и книг, отсортированный по книгам, сортировка по главам произвольная. 
'''

# класс Глава
class Chapter:
    def __init__(self, id, name, page, book_id):
        # номер главы
        self.id = id
        # название главы
        self.name = name
        # страница на которой находится глава
        self.page = page
        # номер книги
        self.book_id = book_id

# класс книга
class Book:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class ChapterBook:
    def __init__(self, book_id, chapter_id):
        self.book_id = book_id
        self.chapter_id = chapter_id


books = [
    Book(1, 'СХЕМЫ АЛГОРИТМОВ, ПРОГРАММ, ДАННЫХ И СИСТЕМ.'),
    Book(2, 'Теоретические основы электротехники. Электрические цепи.'),
    Book(3, 'Английский язык (Для технических университетов и вузов)'),
    Book(4, 'Руководство для начинающих С++. Второе издание'),
    Book(5, 'Архитектура АСОИУ. ЭЛЕМЕНТЫ ТЕОРИИ МНОЖЕСТВ')
]
chapters = [
    Chapter(1, 'Основные положения теории электромагнитного поля и их применение к теории электрических цепей', 8, 2),
    Chapter(2, 'ОПИСАНИЕ СХЕМ', 23, 1),
    Chapter(3, 'Основы С++', 22, 4),
    Chapter(4, 'ОПИСАНИЕ СИМВОЛОВ', 139, 1),
    Chapter(5, 'Не линейные электрические цепи временного тока', 70, 2),
    Chapter(6, 'АРХИЕКТУРНОЕ ПОНЯТИЕ МНОЖЕСТВА', 4, 5)
]
chapters_of_books = [
    ChapterBook(2, 1),
    ChapterBook(1, 2),
    ChapterBook(4, 3),
    ChapterBook(1, 4),
    ChapterBook(2, 5),
    ChapterBook(5, 6),
]


def main():
    one_to_many = [(ch.name, ch.page, book.name)
                   for book in books
                   for ch in chapters
                   if ch.book_id == book.id]

    many_to_many_temp = [(book.name, ChOfBooks.book_id, ChOfBooks.chapter_id)
                         for book in books
                         for ChOfBooks in chapters_of_books
                         if book.id == ChOfBooks.book_id]

    many_to_many = [(ch.name, ch.page, book_name)
                    for book_name, book_id, ch_id in many_to_many_temp
                    for ch in chapters if ch.id == ch_id]

    print('Задание Г1')
    array_dict = {}
    for lib_name, x, book_name in one_to_many:
        # если название книг начинается с 'А'
        if book_name[0] == 'А':
            if book_name in array_dict:
                array_dict[book_name].append(lib_name)
            else:
                array_dict[book_name] = [lib_name]
    print(*array_dict.items())

    print('Задание Г2')
    array_dict_2 = {}
    for x, func_num, book_name in one_to_many:
        if book_name in array_dict_2:
            array_dict_2[book_name] = max(array_dict_2[book_name], func_num)
        else:
            array_dict_2[book_name] = func_num
    array_dict_2 = {key: value for key, value in sorted(array_dict_2.items(), key=lambda item: item[1])}
    print(*array_dict_2.items())

    print('Задание Г3')
    array_list = []
    for lib_name, x, book_name in many_to_many:
        array_list.append((book_name, lib_name))
    array_list = sorted(array_list, key=lambda item: item[0])
    print(*array_list)

if __name__ == '__main__':
    main()