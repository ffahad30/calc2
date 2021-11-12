"""Division Class"""
from calc.operations.calculation import Calculation


class Division(Calculation):
    """ Dividing two numbers"""

    def get_result(self):
        """ divide two numbers and get the result"""
        return self.value_a / self.value_b
