from behave import given, when, then

# @given('Value {A} и {B} are INT value')
@given('Число {A} и {B} является целочисленным типом')
def step_impl(context, A, B):
    if(str(A).isdigit() and str(B).isdigit()):
        pass
        print('OK!')
    else:
        print('Ошибка! Эти не являются числами')


@when('Суммируем {A} и {B}')
def step_impl(context, A, B):
    context.result = int(A) + int(B)
    print('OK!')

@then('Сумма этих чисел равен {C}')
def step_impl(context, C):
    print('OK!')
