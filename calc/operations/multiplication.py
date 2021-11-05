"""Multiplication Class"""
from calculation import Calculation


class Multiplication(Calculation):
    """ Multiplying two numbers"""

    def getResult(self):
        return self.value_a * self.value_b
