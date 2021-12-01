""" This is the increment function"""

from calc.operations.addition import Addition
from calc.operations.subtraction import Subtraction
from calc.operations.multiplication import Multiplication
from calc.operations.division import Division


# pylint: disable=line-too-long


# calculator class and all of its functions only have the methods and properties needed, nothing extra = ISP
# all functions are open for extension but closed for modification ; they cannot be changed = OCP
# separate functions for each of the calculator's math and history operations = SRP
class Calculator:
    """ This is the Calculator class"""

    history = []

    @staticmethod
    def first_calculation_result_in_history() -> int:
        """ return the first result in the calculator's history"""
        return Calculator.history[0].get_result()

    @staticmethod
    def last_calculation_result_in_history() -> int:
        """ return the last result in the calculator's history"""
        return Calculator.history[-1].get_result()

    @staticmethod
    def history_calculations_count() -> int:
        """ count the number of calculation results in the history"""
        return len(Calculator.history)

    @staticmethod
    def clear_calculator_history() -> bool:
        """ clear the calculator's history"""
        Calculator.history.clear()
        return True

    @staticmethod
    def add_numbers(value_a, value_b) -> int:
        """ adds two numbers"""
        addition = Addition.create(value_a, value_b)
        Calculator.history.append(addition)
        return Calculator.last_calculation_result_in_history()

    @staticmethod
    def subtract_numbers(value_a, value_b) -> int:
        """ subtracts a number from result"""
        subtraction = Subtraction.create(value_a, value_b)
        Calculator.history.append(subtraction)
        return Calculator.last_calculation_result_in_history()

    @staticmethod
    def multiply_numbers(value_a, value_b) -> int:
        """ multiplies two numbers"""
        multiplication = Multiplication.create(value_a, value_b)
        Calculator.history.append(multiplication)
        return Calculator.last_calculation_result_in_history()

    @staticmethod
    def divide_numbers(value_a, value_b) -> int:
        """ divides two numbers"""
        division = Division.create(value_a, value_b)
        Calculator.history.append(division)
        return Calculator.last_calculation_result_in_history()
