"""Subtraction Class"""
from calc.operations.calculation import Calculation


class Subtraction(Calculation):
    """ Subtracting two numbers"""

    def get_result(self):
        """ subtract two numbers and get the result"""
        return self.value_a - self.value_b
