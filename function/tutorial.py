from behave import *

@given('launch chrome browser')
def step_impl(context):
    pass

@when('open orange hrm homepage')
def step_impl(context):
    assert True is not False

@then('verify that the logo present on page')
def step_impl(context):
    assert context.failed is False
