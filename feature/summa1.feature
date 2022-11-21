# Example

Feature: Summa A and B part 2
  Здесь применены другие технологии (pytest_bdd)

  Scenario Outline: Сложение целочисленных типов
    # Given Есть класс калькулятор
    # When Суммируем "<A>" и "<B>"
    # Then Сумма этих чисел равен "<C>"
    Given I have a calculator
    When I add "<A>" and "<B>"
    Then the calculator returns "<C>"

    Examples:
      | A | B | C |
      | 1 | 1 | 2 |
      | 2 | 2 | 4 |
      | 3 | 2 | 5 |

