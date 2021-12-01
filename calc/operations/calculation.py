""" This is the abstract base calculation class"""


# pylint: disable=line-too-long
# abstract class not dependent on any details but provides the details for higher level classes = DIP
class Calculation:
    """ calculation class"""

    # pylint: disable=too-few-public-methods
    def __init__(self, value_a, value_b):
        self.value_a = value_a
        self.value_b = value_b

    @classmethod
    def create(cls, value_a, value_b):
        """ factory method """
        return cls(value_a, value_b)
