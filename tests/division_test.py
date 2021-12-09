""" Testing the division function"""
# unit test
# pylint: disable=duplicate-code


from calc.operations.division import Division

from tests import reading_csv
from logs import results_log as log


# division test
def test_calculator_divide_static():
    """testing that the calculator has a static method for division"""
    # pylint: disable=unused-argument,redefined-outer-name
    path = "division.csv"
    columns = reading_csv.reading_csv(path)
    for i in range(len(columns[2])):
        # Arrange
        division = Division(columns[0][i], (columns[1][i],))
        # Act
        # Assert
        assert division.get_result() == columns[2][i]
        log.log_components(path, i, "division", division.get_result())
