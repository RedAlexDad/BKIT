import sys
import math

from function.unique import Unique


def main():
    # Проверка на работоспособность
    data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    print(data)
    a = Unique(data)
    for i in Unique(a):
        print(i, end=' ')
    print()


# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()
