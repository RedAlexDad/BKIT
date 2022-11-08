# Итератор для удаления дубликатов
from gen_random import *
from convert import *
import sys

class Unique(object):
    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор
        # должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться
        # одинаковыми строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ - разные строки
        #           ignore_case = False, Aбв и АБВ - одинаковые строки,
        #           одна из которых удалится
        # По-умолчанию ignore_case = False

        self.arr = []

        # используя кортежи, получаем ключ и значения
        for key, value in kwargs.items():
            # если ключ пустой и значение ИСТИНА, то
            if key == 'ignore_case' and value == True:
                # в текущем списке все символы преобразуем в нижний регистр через функции lower
                items = [i.lower() for i in items]

        for index in items:
            # Если текущее значение с списка item не совпадает / не существует в созданном списке arr
            if index not in self.arr:
                # то присвоем несуществующее значение в созданном списке arr
                self.arr.append(index)
        pass

    def __next__(self):
        try:
            x = self.arr[self.begin]
            self.begin += 1
            return x
        except:
            raise StopIteration

    def __iter__(self):
        self.begin = 0
        return self
def main():
    print('Задача №3 - unique.py')
    data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    print(data)
    a = Unique(data)
    for i in Unique(a):
        print(i, end=' ')
    print()

    data1 = gen_random(10, 1, 3)
    print(data1)
    b = Unique(data1)
    for i in Unique(b):
        print(i, end=' ')
    print()

    data2 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    print(data2)
    c = Unique(data2)
    for i in Unique(c):
        print(i, end=' ')
    print()

    d = Unique(data2, ignore_case=True)
    for i in Unique(d):
        print(i, end=' ')
    print()

    if (len(sys.argv) == 1):
        data3 = into_tuple_from_str(input('Введите любой символ списка: '))
        print(data3)
        c = Unique(data3)
        print('Без чувствительного регистра')
        for i in Unique(c):
            print(i, end=' ')
        print()

        print(data3)
        c = Unique(data3, ignore_case=True)
        print('С чувствительным регистром')
        for i in Unique(c):
            print(i, end=' ')
        print()

    elif (len(sys.argv) > 1):
        buff = sys.argv[1]
        for i in range(2, len(sys.argv)):
            buff = buff + ' ' + sys.argv[i]

        data3 = into_tuple_from_str(buff)

        print(data3)
        c = Unique(data3)
        print('С чувствительным регистром')
        for i in Unique(c):
            print(i, end=' ')
        print()

        print(data3)
        c = Unique(data3, ignore_case=True)
        print('Без чувствительного регистра')
        for i in Unique(c):
            print(i, end=' ')
        print()
    else:
        print('Ошибка введения аргументов!')



if __name__ == "__main__":
    main()