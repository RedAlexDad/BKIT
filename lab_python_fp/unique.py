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
        self.items = items
        self.kwargs = kwargs

    def __next__(self):
        return self.items

    def __iter__(self):
        return self


class FRange:
    def __init__(self, start=0.0, stop=0.0, step=1.0):
        self.start = start
        self.stop = stop
        self.step = step
        self.value = self.start - self.step
    def __iter__(self):
        self.value = self.start - self.step
        return self
    def __next__(self):
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration
