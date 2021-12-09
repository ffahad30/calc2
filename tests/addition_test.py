""" Testing the addition function"""
# unit test
# pylint: disable=duplicate-code

from calc.operations.addition import Addition

from tests import reading_csv
from results import results_log as log


# addition test
def test_calculator_add_static():
    """testing that the calculator has a static method for addition"""
    # pylint: disable=unused-argument,redefined-outer-name
    path = "addition.csv"
    columns = reading_csv.reading_csv(path)
    for i in range(len(columns[2])):
        # Arrange
        addition = Addition(columns[0][i], (columns[1][i],))
        # Act
        # Assert
        assert addition.get_result() == columns[2][i]
        log.log_components(path, i, "addition", addition.get_result())
