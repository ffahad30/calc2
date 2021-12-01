""" This is the abstract base calculation class"""


# calculator operations inherit value_a and value_b from Calculation class = inheritance
# abstraction
class Calculation:
    """ calculation class"""

    def __init__(self, value_a, value_b):
        self.value_a = value_a
        self.value_b = value_b

    @classmethod
    def create(cls, value_a, value_b):
        """ factory method """
        return cls(value_a, value_b)
