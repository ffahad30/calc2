""" Testing the division function's ZeroDivisionError exception"""
# unit test
# pylint: disable=duplicate-code
from pprint import pprint


from calc.operations.division import Division

from tests import reading_csv
from results import error_log as log


# division error test
def test_calculator_divide_error_static():
    """testing that the calculator throws an exception for the ZeroDivisionError"""
    # pylint: disable=unused-argument,redefined-outer-name
    path = "division_error.csv"
    columns = reading_csv.reading_csv(path)
    for i in range(len(columns[2])):
        # Arrange
        division = Division(columns[0][i], (columns[1][i]))
        # Act
        # Assert
        assert division.get_result() == columns[2][i]
        log.log_errors(path, i)
