"""Multiplication Class"""
from calc.operations.calculation import Calculation


class Multiplication(Calculation):
    """ Multiplying two numbers"""

    def get_result(self):
        """ multiply two numbers and get the result"""
        return self.value_a * self.value_b
