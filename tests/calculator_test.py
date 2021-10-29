"""Testing the Calculator"""
from calc.calculator import Calculator


def test_calculator_add_static():
    """testing that our calculator had a static method for addition"""
    assert Calculator.add_numbers(1, 2) == 3


def test_calculator_subtract_static():
    """testing that our calculator had a static method for subtraction"""
    assert Calculator.subtract_numbers(2, 1) == 1


def test_calculator_multiply_static():
    """testing that our calculator had a static method for multiplication"""
    assert Calculator.multiply_numbers(1, 2) == 2


def test_calculator_divide_static():
    """testing that our calculator had a static method for division"""
    assert Calculator.divide_numbers(2, 1) == 2
