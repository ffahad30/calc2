""" Testing the multiplication function"""
# unit test
# pylint: disable=duplicate-code
from pprint import pprint


from calc.calculator import Calculator


# multiplication test
def test_calculator_multiply_static():
    """testing that the calculator has a static method for multiplication"""
    # pylint: disable=unused-argument,redefined-outer-name
    # Act
    # Assert
    assert Calculator.multiply_numbers(1, 2) == 2
    assert Calculator.multiply_numbers(4, 5) == 20
    assert Calculator.multiply_numbers(6, 2) == 12
    assert Calculator.multiply_numbers(3, 6) == 18
    assert Calculator.history_calculations_count() == 4
    assert Calculator.first_calculation_result_in_history() == 2
    assert Calculator.last_calculation_result_in_history() == 18
    # "float(float(Calculator.last_calculation_result_in_history())" is a type cast
    assert float(Calculator.last_calculation_result_in_history()) == 18.0
    pprint(Calculator.history)
