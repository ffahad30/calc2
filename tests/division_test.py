"""Testing Division"""
from calc.operations.division import Division


def test_division():
    """testing calc result is 2"""
    assert Division.divide(2, 1) == 2
