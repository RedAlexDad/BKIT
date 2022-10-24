from .gen_random import *

# Итератор для удаления дубликатов
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
