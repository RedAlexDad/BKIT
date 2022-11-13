def simple_value(value):
    if value > 1:
        for i in range(2, int(value / 2) + 1):
            if (value % i) == 0:
                return "Это число не является простым"
                break
        else:
            return "Это число является простым"

    elif(value == 1):
        return "Это число не является ни простым, ни составным числом"
    else:
        return "Нулевое число не является простым"