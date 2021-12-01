""" Testing the division function"""
# unit test
# pylint: disable=duplicate-code
from pprint import pprint


from calc.calculator import Calculator


# division test
def test_calculator_divide_static():
    """testing that the calculator has a static method for division"""
    # pylint: disable=unused-argument,redefined-outer-name
    # Act
    # Assert
    assert Calculator.divide_numbers(6, 2) == 3
    assert Calculator.divide_numbers(10, 5) == 2
    assert Calculator.divide_numbers(30, 6) == 5
    assert Calculator.divide_numbers(14, 2) == 7
    assert Calculator.divide_numbers(9, 3) == 3
    assert Calculator.history_calculations_count() == 5
    assert Calculator.first_calculation_result_in_history() == 3
    assert Calculator.last_calculation_result_in_history() == 3
    assert float(Calculator.last_calculation_result_in_history()) == 3.0
    pprint(Calculator.history)
