Feature: Calculating and getting unique values

   # Уникальные значения числового типа
   # If <CASE> is 1 then is True
  Scenario Outline: We get unique values from the list of the contained number
    Given I have a class of unique values
    And Getting the list: <list>
    When Finding unique values, case: <CASE>
    Then Output unique values: <unique>

    Examples:
      | list                           | unique    | CASE |
      | [1, 1, 1, 1, 1, 2, 2, 2, 2, 2] | [1, 2]    | 0    |
      | [1, 3, 1, 1, 1, 3, 2, 2, 2, 2] | [1, 3, 2] | 0    |


   # Уникальные значения символьного типа
  Scenario Outline: We get unique values from the list of the contained char
    Given I have a class of unique values
    And Getting the list: <list>
    When Finding unique values, case: <CASE>
    Then Output unique values: <unique>

    Examples:
      | list                                     | unique                         | CASE |
      | ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B'] | ['a', 'A', 'b', 'B']           | 0    |
      | ['a', 'C', 'b', 'B', 'c', 'A', 'b', 'B'] | ['a', 'C', 'b', 'B', 'c', 'A'] | 0    |


   # Уникальные значения символьного типа без чувствительного регистра
  Scenario Outline: We get unique values from the list of the contained char ignore_case
    Given I have a class of unique values
    And Getting the list: <list>
    When Finding unique values, case: <CASE>
    Then Output unique values: <unique>

    Examples:
      | list                                     | unique          | CASE |
      | ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B'] | ['a', 'b']      | 1    |
      | ['a', 'C', 'b', 'B', 'c', 'A', 'b', 'B'] | ['a', 'c', 'b'] | 1    |


   # Уникальные значения смешанного типа
  Scenario Outline: We get unique values from the list of the contained all type
    Given I have a class of unique values
    And Getting the list: <list>
    When Finding unique values, case: <CASE>
    Then Output unique values: <unique>

    Examples:
      | list                                     | unique                         | CASE |
      | ['a', 'A', 'b', 'B', '1', '1', '2', '2'] | ['a', 'A', 'b', 'B', '1', '2'] | 0    |
      | ['a', 'A', 'b', 'B', '1', '1', '2', '2'] | ['a', 'b', '1', '2']           | 1    |