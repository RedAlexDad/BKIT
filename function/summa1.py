# from pytest_bdd import given, when, then, scenarios, parsers
from behave   import given, when, then, register_type
# scenarios("summa1.feature")
from feature.steps.calculator import Calculator
from hamcrest import assert_that, equal_to

def parse_number(text):
    """
    Convert parsed text into a number.
    :param text: Parsed text, called by :py:meth:`parse.Parser.parse()`.
    :return: Number instance (integer), created from parsed text.
    """
    return int(text)
# -- REGISTER: User-defined type converter (parse_type).
register_type(Number=parse_number)

# @given(parsers.parse('Число {A:d} является целочисленным типом'), target_fixture = 'coefA')
# @given(parsers.parse("The A coefficient {A:d}"), target_fixture = 'coefA')
@given('I have a calculator')
def step_impl(context):
    context.calculator = Calculator()


@when('I add "{x:Number}" and "{y:Number}"')
def step_impl(context, A, B):
    assert isinstance(A, int)
    assert isinstance(B, int)
    context.calculator.add2(A, B)

@then('the calculator returns "{expected:Number}"')
def step_impl(context, C):
    assert isinstance(C, int)
    assert_that(context.calculator.result, equal_to(C))