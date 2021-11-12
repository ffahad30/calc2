""" This is the abstract base calculation class"""


class Calculation:
    """ calculation class"""
    # pylint: disable=too-few-public-methods
    # default constructor
    def __init__(self, value_a, value_b):
        self.value_a = value_a
        self.value_b = value_b

    @classmethod
    def create(cls, value_a, value_b):
        """ create abstract class method"""
        return cls(value_a, value_b)
