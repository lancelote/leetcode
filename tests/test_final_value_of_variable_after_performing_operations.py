import pytest

from src.final_value_of_variable_after_performing_operations import Solution


@pytest.mark.parametrize(
    "operations,expected_result",
    [
        (["--X", "X++", "X++"], 1),
        (["++X", "++X", "X++"], 3),
        (["X++", "++X", "--X", "X--"], 0),
    ],
)
def test_solution(operations, expected_result):
    assert Solution().finalValueAfterOperations(operations) == expected_result
