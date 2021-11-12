"""Addition Class"""
from calc.operations.calculation import Calculation


class Addition(Calculation):
    """ Adding two numbers"""

    def get_result(self):
        """ add two numbers and get the result"""
        return self.value_a + self.value_b
