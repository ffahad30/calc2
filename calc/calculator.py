""" This is the increment function"""

from calc.operations.addition import Addition
from calc.operations.subtraction import Subtraction
from calc.operations.multiplication import Multiplication
from calc.operations.division import Division


class Calculator:
    """ This is the Calculator class"""

    history = []

    @staticmethod
    def first_calculation_result_in_history():
        """ return the first result in the calculator's history"""
        return Calculator.history[0].get_result()

    @staticmethod
    def last_calculation_result_in_history():
        """ return the last result in the calculator's history"""
        return Calculator.history[-1].get_result()

    @staticmethod
    def history_calculations_count():
        """ count the number of calculation results in the history"""
        return len(Calculator.history)

    @staticmethod
    def clear_calculator_history():
        """ clear the calculator's history"""
        Calculator.history.clear()
        return True

    @staticmethod
    def add_numbers(value_a, value_b):
        """ adds two numbers"""
        addition = Addition.create(value_a, value_b)
        Calculator.history.append(addition)
        return Calculator.last_calculation_result_in_history()

    @staticmethod
    def subtract_numbers(value_a, value_b):
        """ subtracts a number from result"""
        subtraction = Subtraction.create(value_a, value_b)
        Calculator.history.append(subtraction)
        return Calculator.last_calculation_result_in_history()

    @staticmethod
    def multiply_numbers(value_a, value_b):
        """ multiplies two numbers"""
        multiplication = Multiplication.create(value_a, value_b)
        Calculator.history.append(multiplication)
        return Calculator.last_calculation_result_in_history()

    @staticmethod
    def divide_numbers(value_a, value_b):
        """ divides two numbers"""
        division = Division.create(value_a, value_b)
        Calculator.history.append(division)
        return Calculator.last_calculation_result_in_history()
