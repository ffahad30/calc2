"""Addition Class"""
from calc.operations.calculation import Calculation


# class
# Subclass #1 in facade pattern
class Addition(Calculation):
    """ Adding two numbers"""
    # pylint: disable=line-too-long
    def get_result(self):
        """ add two numbers and get the result"""
        # result is in a namespace
        result = self.value_a + self.value_b
        return result
