import pytest
from src.squares_of_a_sorted_array import Solution


@pytest.mark.parametrize(
    "array, expected",
    [
        ([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100]),
        ([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121]),
    ],
)
def test_basic_examples(array, expected):
    assert Solution().sortedSquares(array) == expected
