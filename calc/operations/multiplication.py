"""Multiplication Class"""
from calc.operations.calculation import Calculation


# class
# Subclass #3 in facade pattern
class Multiplication(Calculation):
    """ Multiplying two numbers"""
    # pylint: disable=line-too-long
    def get_result(self):
        """ multiply two numbers and get the result"""
        # result is in a namespace
        result = self.value_a * self.value_b
        return result
