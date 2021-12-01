""" Testing the addition function"""
# unit test
# pylint: disable=duplicate-code
from pprint import pprint


from calc.calculator import Calculator


# addition test
def test_calculator_add_static():
    """testing that the calculator has a static method for addition"""
    # pylint: disable=unused-argument,redefined-outer-name
    # Act
    # Assert
    assert Calculator.add_numbers(1, 2) == 3
    assert Calculator.add_numbers(2, 5) == 7
    assert Calculator.history_calculations_count() == 2
    assert Calculator.first_calculation_result_in_history() == 3
    assert Calculator.last_calculation_result_in_history() == 7
    # "float(float(Calculator.last_calculation_result_in_history())" is a type cast
    assert float(Calculator.last_calculation_result_in_history()) == 7.0
    pprint(Calculator.history)
