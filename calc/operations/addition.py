"""Addition Class"""
from calc.operations.calculation import Calculation


class Addition(Calculation):
    """ Adding two numbers"""
    # pylint: disable=line-too-long
    def get_result(self):
        """ add two numbers and get the result"""
        # value_a and value_b are seamlessly inherited from calculation class = LSP
        result = self.value_a + self.value_b
        return result
