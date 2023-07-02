import pytest

from src.unique_number_of_occurrences import Solution


@pytest.mark.parametrize(
    "arr,expected",
    (
        ([1, 2, 2, 1, 1, 3], True),
        ([1, 2], False),
        ([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0], True),
    ),
)
def test_solution(arr, expected):
    assert Solution().uniqueOccurrences(arr) == expected
