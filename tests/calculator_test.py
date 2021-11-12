"""Testing the Calculator"""

from pprint import pprint


from calc.calculator import Calculator


def test_calculator_add_static():
    """testing that the calculator has a static method for addition"""
    Calculator.history.clear()
    assert Calculator.add_numbers(1, 2) == 3
    assert Calculator.add_numbers(2, 5) == 7
    assert Calculator.history_calculations_count() == 2
    assert Calculator.first_calculation_result_in_history() == 3
    assert Calculator.last_calculation_result_in_history() == 7
    pprint(Calculator.history)


def test_calculator_subtract_static():
    """testing that the calculator has a static method for subtraction"""
    Calculator.history.clear()
    assert Calculator.subtract_numbers(2, 1) == 1
    assert Calculator.subtract_numbers(7, 2) == 5
    assert Calculator.subtract_numbers(5, 2) == 3
    assert Calculator.history_calculations_count() == 3
    assert Calculator.first_calculation_result_in_history() == 1
    assert Calculator.last_calculation_result_in_history() == 3
    pprint(Calculator.history)


def test_calculator_multiply_static():
    """testing that the calculator has a static method for multiplication"""
    Calculator.history.clear()
    assert Calculator.multiply_numbers(1, 2) == 2
    assert Calculator.multiply_numbers(4, 5) == 20
    assert Calculator.multiply_numbers(6, 2) == 12
    assert Calculator.multiply_numbers(3, 6) == 18
    assert Calculator.history_calculations_count() == 4
    assert Calculator.first_calculation_result_in_history() == 2
    assert Calculator.last_calculation_result_in_history() == 18
    pprint(Calculator.history)


def test_calculator_divide_static():
    """testing that the calculator has a static method for division"""
    Calculator.history.clear()
    assert Calculator.divide_numbers(6, 2) == 3
    assert Calculator.divide_numbers(10, 5) == 2
    assert Calculator.divide_numbers(30, 6) == 5
    assert Calculator.divide_numbers(14, 2) == 7
    assert Calculator.divide_numbers(9, 3) == 3
    assert Calculator.history_calculations_count() == 5
    assert Calculator.first_calculation_result_in_history() == 3
    assert Calculator.last_calculation_result_in_history() == 3
    pprint(Calculator.history)


def test_clear_calculator_history():
    """ testing the clear history function of the calculator"""
    Calculator.history.clear()
    assert Calculator.add_numbers(1, 2) == 3
    assert Calculator.add_numbers(2, 5) == 7
    assert Calculator.history_calculations_count() == 2
    assert Calculator.clear_calculator_history() is True
    assert Calculator.history_calculations_count() == 0


def test_history_calculations_count():
    """ testing that the calculator can count the number of calculation results in history"""
    Calculator.history.clear()
    assert Calculator.add_numbers(1, 2) == 3
    assert Calculator.add_numbers(2, 4) == 6
    assert Calculator.history_calculations_count() == 2


def test_first_calculation_result_in_history():
    """ testing that the calculator can return the first calculation result in history"""
    Calculator.history.clear()
    assert Calculator.add_numbers(1, 2) == 3
    assert Calculator.add_numbers(2, 4) == 6
    assert Calculator.first_calculation_result_in_history() == 3


def test_last_calculation_result_in_history():
    """ testing that the calculator can return the last calculation result in history"""
    Calculator.history.clear()
    assert Calculator.add_numbers(1, 2) == 3
    assert Calculator.add_numbers(2, 4) == 6
    assert Calculator.last_calculation_result_in_history() == 6
