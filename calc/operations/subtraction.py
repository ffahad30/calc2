"""Subtraction Class"""
from calc.operations.calculation import Calculation


# class
# Subclass #2 in facade pattern
class Subtraction(Calculation):
    """ Subtracting two numbers"""
    # pylint: disable=line-too-long
    def get_result(self):
        """ subtract two numbers and get the result"""
        # result is in a namespace
        result = self.value_a - self.value_b
        return result
