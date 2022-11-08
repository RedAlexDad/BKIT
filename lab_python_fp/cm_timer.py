'''
Необходимо написать контекстные менеджеры cm_timer_1 и cm_timer_2,
которые считают время работы блока кода и выводят его на экран.
Пример:

with cm_timer_1():
    sleep(5.5)

После завершения блока кода в консоль должно вывестись time: 5.5
(реальное время может несколько отличаться).

cm_timer_1 и cm_timer_2 реализуют одинаковую функциональность,
но должны быть реализованы двумя различными способами
(на основе класса и с использованием библиотеки contextlib).
'''

from time import time, sleep
from contextlib import contextmanager

# С использованием класса
class cm_timer_1:
    def __int__(self):
        self._start = 0
        self._end = 0

    def __enter__(self):
        self._start = time()

    def __exit__(self, the_type, the_value, the_backing):
        self._end = time()
        print(f'Time of work: {self._end - self._start}')

# С использованием библитоеки contextlib
@contextmanager
def cm_timer_2():
    start_time = time()
    yield None
    end_time = time()
    print(f'Time of work: {end_time - start_time}')

def main():
    with cm_timer_1():
        sleep(5.5)

    with cm_timer_2():
        sleep(5.5)

if __name__ == "__main__":
    main()