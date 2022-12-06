
class the_simplest_mathematical_calculator(object):
    '''
    def __init__(self):
        self.math_calculation = ''
        self.math_calculation_list = []
        self.list_enumeration_sign = []
        self.type_error = ''
        self.result = None

    '''
    def __init__(self, math_calculate):
        self.math_calculation = math_calculate
        self.math_calculation_list = self.delete_space_into_list(math_calculate)
        self.list_enumeration_sign = self.enumeration_sign(self.math_calculation_list)

        self.type_error = None

        for sgin in self.list_enumeration_sign:
            self.arifmetic(sgin, self.math_calculation_list)

        if(self.type_error == None):
            self.result = float(self.math_calculation_list[0])


    # Преобразование строкого типа в list
    def delete_space_into_list(self, str_calculate):
        new_str = []
        str_value = ''
        for i in str_calculate:
            if(i != ' '):
                str_value += i
            else:
                new_str.append(str_value)
                str_value = ''

        new_str.append(str_value)

        return new_str


    # Расстановка приоритета операции
    def enumeration_sign(self, list_str):
        count_list = []
        for i in list_str:
            if ('*' == i): count_list.append(i)
            if ('/' == i): count_list.append(i)
            if ('+' == i): count_list.append(i)
            if ('-' == i): count_list.append(i)

        count_list = self.prioritet(count_list)

        return count_list

    # Поддержка функции по расстановку приоритета операции
    def prioritet(self, list_str):
        new_list = []
        size = len(list_str)
        count = 0
        while (size != 0):
            if('*' in list_str or '/' in list_str):
                for i in list_str:
                    if(i == '*' or i == '/'):
                        new_list.append(i)
                size -= 1
            if('+' in list_str or '-' in list_str):
                for i in list_str:
                    if(i == '+' or i == '-'):
                        new_list.append(i)
                size -= 1

        return new_list

    # Арифметические операции
    def arifmetic(self, sign, list):
        result = None
        if (sign in list):
            for i in range(1, len(list) - 1):
                try:
                    if(list[i] == sign):
                        if(sign == '*'): result = float(list[i - 1]) * float(list[i + 1])
                        elif(sign == '/'): result = float(list[i - 1]) / float(list[i + 1])
                        elif (sign == '+'): result = float(list[i - 1]) + float(list[i + 1])
                        elif (sign == '-'): result = float(list[i - 1]) - float(list[i + 1])

                        list[i] = result
                        del list[i - 1: i]
                        del list[i: i + 1]

                # Деление на 0
                except ZeroDivisionError:
                    self.type_error = 'Division by 0'
                    self.result = 'inf'

                # Граница вне диапазона
                except:
                    return result

    def calculate(self, math_calculate):
        self.math_calculation = math_calculate
        self.math_calculation_list = self.delete_space_into_list(math_calculate)
        self.list_enumeration_sign = self.enumeration_sign(self.math_calculation_list)

        self.type_error = None

        for sgin in self.list_enumeration_sign:
            self.arifmetic(sgin, self.math_calculation_list)

        if(self.type_error == None):
            self.result = float(self.math_calculation_list[0])

        return self