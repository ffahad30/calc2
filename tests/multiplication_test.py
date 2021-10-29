"""Testing Multiplication"""
from calc.operations.multiplication import Multiplication


def test_multiplication():
    """testing calc result is 2"""
    assert Multiplication.multiply(1, 2) == 2
