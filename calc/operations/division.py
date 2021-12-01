"""Division Class"""
from calc.operations.calculation import Calculation


class Division(Calculation):
    """ Dividing two numbers"""

    # pylint: disable=line-too-long
    def get_result(self):
        """ divide two numbers and get the result"""
        result = self.value_a / self.value_b
        return result
