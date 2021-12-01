""" Testing the subtraction function"""
# unit test
# pylint: disable=duplicate-code
from pprint import pprint


from calc.calculator import Calculator


# subtraction test
def test_calculator_subtract_static():
    """testing that the calculator has a static method for subtraction"""
    # pylint: disable=unused-argument,redefined-outer-name
    # Arrange
    Calculator.history.clear()
    # Act
    # Assert
    assert Calculator.subtract_numbers(2, 1) == 1
    assert Calculator.subtract_numbers(7, 2) == 5
    assert Calculator.subtract_numbers(5, 2) == 3
    assert Calculator.history_calculations_count() == 3
    assert Calculator.first_calculation_result_in_history() == 1
    assert Calculator.last_calculation_result_in_history() == 3
    # "float((Calculator.last_calculation_result_in_history())" is a type cast
    assert float(Calculator.last_calculation_result_in_history()) == 3.0
    pprint(Calculator.history)
