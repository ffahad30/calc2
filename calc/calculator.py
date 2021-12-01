""" This is the increment function"""

from calc.operations.addition import Addition
from calc.operations.subtraction import Subtraction
from calc.operations.multiplication import Multiplication
from calc.operations.division import Division


# pylint: disable=line-too-long


# static class
# main class in facade pattern which inherits Addition, Subtraction, Multiplication, and Subtraction classes
class Calculator:
    """ This is the Calculator class"""

    # object
    history = []

    # static method
    @staticmethod
    # "-> int" is a type hint
    def first_calculation_result_in_history() -> int:
        """ return the first result in the calculator's history"""
        return Calculator.history[0].get_result()

    # static method
    @staticmethod
    # "-> int" is a type hint
    def last_calculation_result_in_history() -> int:
        """ return the last result in the calculator's history"""
        return Calculator.history[-1].get_result()

    # static method
    @staticmethod
    # "-> int" is a type hint
    def history_calculations_count() -> int:
        """ count the number of calculation results in the history"""
        # len() is a list method
        return len(Calculator.history)

    # static method
    @staticmethod
    # "-> bool" is a type hint
    def clear_calculator_history() -> bool:
        """ clear the calculator's history"""
        # clear() is a list method
        Calculator.history.clear()
        return True

    # static method
    @staticmethod
    # "-> int" is a type hint
    def add_numbers(value_a, value_b) -> int:
        """ adds two numbers"""
        addition = Addition.create(value_a, value_b)
        # append() is a list method
        Calculator.history.append(addition)
        return Calculator.last_calculation_result_in_history()

    # static method
    @staticmethod
    # "-> int" is a type hint
    def subtract_numbers(value_a, value_b) -> int:
        """ subtracts a number from result"""
        subtraction = Subtraction.create(value_a, value_b)
        # append() is a list method
        Calculator.history.append(subtraction)
        return Calculator.last_calculation_result_in_history()

    # static method
    @staticmethod
    # "-> int" is a type hint
    def multiply_numbers(value_a, value_b) -> int:
        """ multiplies two numbers"""
        multiplication = Multiplication.create(value_a, value_b)
        # append() is a list method
        Calculator.history.append(multiplication)
        return Calculator.last_calculation_result_in_history()

    # static method
    @staticmethod
    # "-> int" is a type hint
    def divide_numbers(value_a, value_b) -> int:
        """ divides two numbers"""
        division = Division.create(value_a, value_b)
        # append() is a list method
        Calculator.history.append(division)
        return Calculator.last_calculation_result_in_history()
