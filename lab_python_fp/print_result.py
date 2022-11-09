'''
Необходимо реализовать декоратор print_result,
который выводит на экран результат выполнения функции.

Декоратор должен принимать на вход функцию, вызывать её,
печатать в консоль имя функции и результат выполнения,
после чего возвращать результат выполнения.
Если функция вернула список (list),
то значения элементов списка должны выводиться в столбик.
Если функция вернула словарь (dict),
то ключи и значения должны выводить в столбик через знак равенства.

Шаблон реализации:

Результат выполнения:
test_1
1
test_2
iu5
test_3
a = 1
b = 2
test_4
1
2
'''

# Здесь должна быть реализация декоратора

# Синтаксис для обертывания функции в декоратор


def print_result(function):
    def control(arr=[], *args, **kwargs):
        # печатает название вызываемой функции
        print(function.__name__)
        if len(arr) == 0:
            result = function(*args, **kwargs)
        else:
            result = function(arr, *args, **kwargs)

        '''if type(result) is not int and type(result) is not float:
            if type(result[0]) is tuple:
                for arr_item_index in range(len(result)):
                    word = ''
                    for item in result[arr_item_index]:
                        word = word + ' ' + item
                    word = word.replace(' ', '', 1)
                    result[arr_item_index] = word'''

        if type(result) == int or type(result) == str:
            print(result)
        elif type(result) is list:
            print('\n'.join(map(str, result)))
        elif type(result) is dict:
            for key, el in result.items():
                print(f'{key} = {el}')
        elif type(result) == zip:
            for name, number in result:
                print(name, number)
        else:
            print(result)
        return result
    return control

@print_result
def test_1():
    return 1

@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]

def main():
    test_1()
    test_2()
    test_3()
    test_4()

if __name__ == "__main__":
    main()