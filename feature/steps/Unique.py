from behave import Given, When, Then
from function.Unique import Unique
import ast


@Given('I have a class of unique values')
def step_impl(context):
    pass


@Given("Getting the list: {LIST}")
def given_increment(context, LIST):
    context.LIST = list(ast.literal_eval(LIST))
    print(f'Список: {LIST}')


@When("Finding unique values, case: {CASE}")
def given_increment(context, CASE):
    check = bool(int(CASE))
    if (check == True):
        unique_list = Unique(context.LIST, ignore_case=check)
    else:
        unique_list = Unique(context.LIST)

    context.results = unique_list
    # print(f'Уникальные значения: {unique_list}')


@Then("Output unique values: {UNIQUE}")
def then_results(context, UNIQUE):
    assert context.results.arr == ast.literal_eval(UNIQUE)
    print(f'Уникальные значения: {context.results.arr}')
