"""Testing Subtraction"""
from calc.operations.subtraction import Subtraction


def test_subtraction():
    """testing calc result is 1"""
    assert Subtraction.subtract(2, 1) == 1
