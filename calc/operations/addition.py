"""Addition Class"""
from calculation import Calculation


class Addition(Calculation):
    """ Adding two numbers"""

    def getResult(self):
        return self.value_a + self.value_b
