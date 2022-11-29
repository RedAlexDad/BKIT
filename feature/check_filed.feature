Feature: Checking the output of an argument from the goods dictionaries


  # Проверка вывода с 1 аргумента
  Scenario Outline: Checking the output with 1 argument
    Given I have a dictionary goods
    When We enter <arguments> to get the desired values
    Then Output to the <check_result>

    Examples:
      | arguments | check_result                                       |
      | title     | [{'title': 'Ковер'},{'title': 'Диван для отдыха'}] |
      | color     | [{'color': 'green'},{'color': 'black'}]            |
      | price     | [{'price': 2000},{'price': 5300}]                  |


      # Проверка вывода с 2 аргумента
  Scenario Outline: Checking the output with 2 argument
    Given I have a dictionary goods
    When We enter <arguments> to get the desired values
    Then Output to the <check_result>

    Examples:
      | arguments   | check_result                                                                           |
      | title color | [{'title': 'Ковер', 'color': 'green'},{'title': 'Диван для отдыха', 'color': 'black'}] |
      | color price | [{'color': 'green', 'price': 2000},{'color': 'black', 'price': 5300}]                  |


      # Проверка вывода с 3 аргумента
  Scenario Outline: Checking the output with 3 argument
    Given I have a dictionary goods
    When We enter <arguments> to get the desired values
    Then Output to the <check_result>

    Examples:
      | arguments         | check_result                                                                                                          |
      | title color price | [{'color': 'green', 'price': 2000, 'title': 'Ковер'}, {'color': 'black', 'price': 5300, 'title': 'Диван для отдыха'}] |