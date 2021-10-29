"""Testing Addition"""
from calc.operations.addition import Addition


def test_addition():
    """testing calc result is 3"""
    assert Addition.add(1, 2) == 3
