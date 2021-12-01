"""Subtraction Class"""
from calc.operations.calculation import Calculation


class Subtraction(Calculation):
    """ Subtracting two numbers"""
    # pylint: disable=line-too-long
    # get_result is used in the Addition, Subtraction, Multiplication, & Division classes = polymorphism
    def get_result(self):
        """ subtract two numbers and get the result"""
        result = self.value_a - self.value_b
        return result
