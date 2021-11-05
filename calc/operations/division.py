"""Division Class"""
from calculation import Calculation


class Division(Calculation):
    """ Dividing two numbers"""

    def getResult(self):
        return self.value_a / self.value_b
