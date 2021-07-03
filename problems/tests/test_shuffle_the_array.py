import pytest
from src.shuffle_the_array import Solution


@pytest.mark.parametrize(
    "array,n,expected",
    [
        ([2, 5, 1, 3, 4, 7], 3, [2, 3, 5, 4, 1, 7]),
        ([1, 2, 3, 4, 4, 3, 2, 1], 4, [1, 4, 2, 3, 3, 2, 4, 1]),
        ([1, 1, 2, 2], 2, [1, 2, 1, 2]),
    ],
)
def test_solution(array, n, expected):
    assert Solution().shuffle(array, n) == expected
