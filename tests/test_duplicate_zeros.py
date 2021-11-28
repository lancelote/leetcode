import pytest

from src.duplicate_zeros import Solution


@pytest.mark.parametrize(
    "arr,expected",
    [
        ([1, 0, 2, 3, 0, 4, 5, 0], [1, 0, 0, 2, 3, 0, 0, 4]),
        ([1, 2, 3], [1, 2, 3]),
    ],
)
def test_solution(arr, expected):
    Solution().duplicateZeros(arr)
    assert arr == expected
