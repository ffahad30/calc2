"""Subtraction Class"""
from calculation import Calculation


class Subtraction(Calculation):
    """ Subtracting two numbers"""

    def getResult(self):
        return self.value_a - self.value_b
