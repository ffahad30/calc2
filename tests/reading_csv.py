"""Reading the CSV files"""
# pylint: disable=invalid-name

import pandas as pd


def reading_csv(path):
    """Reading the logs of the addition, subtraction, multiplication, and division CSV files"""
    x = pd.read_csv(path)
    value_1 = x['VALUE 1']
    value_2 = x['VALUE 2']
    result = x['RESULT']
    return value_1, value_2, result
