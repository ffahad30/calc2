""" Testing the multiplication function"""
# unit test
# pylint: disable=duplicate-code

from calc.operations.multiplication import Multiplication

from tests import reading_csv
from results import results_log as log


# multiplication test
def test_calculator_multiply_static():
    """testing that the calculator has a static method for multiplication"""
    # pylint: disable=unused-argument,redefined-outer-name
    path = "multiplication.csv"
    columns = reading_csv.reading_csv(path)
    for i in range(len(columns[2])):
        # Arrange
        multiplication = Multiplication(columns[0][i], (columns[1][i]))
        # Act
        # Assert
        assert multiplication.get_result() == columns[2][i]
        log.log_components(path, i, "multiplication", multiplication.get_result())
