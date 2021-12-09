""" Testing the subtraction function"""
# unit test
# pylint: disable=duplicate-code


from calc.operations.subtraction import Subtraction

from tests import reading_csv
from results import results_log as log


# subtraction test
def test_calculator_subtract_static():
    """testing that the calculator has a static method for addition"""
    # pylint: disable=unused-argument,redefined-outer-name
    path = "subtraction.csv"
    columns = reading_csv.reading_csv(path)
    for i in range(len(columns[2])):
        # Arrange
        subtraction = Subtraction(columns[0][i], (columns[1][i],))
        # Act
        # Assert
        assert subtraction.get_result() == columns[2][i]
        log.log_components(path, i, "subtraction", subtraction.get_result())
