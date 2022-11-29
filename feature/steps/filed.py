from behave import Given, When, Then
from function.filed import field, goods
import ast

@Given('I have a dictionary goods')
def step_impl(context):
    context.data_dictonary = goods
    test = context.data_dictonary
    print(test)


@When("We enter {arguments} to get the desired values")
def given_increment(context, arguments):
    context.results = field(context.data_dictonary, arguments)


@Then("Output to the {check_result}")
def then_results(context, check_result):
    assert context.results == ast.literal_eval(check_result)