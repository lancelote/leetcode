import pytest

from src.sort_integers_by_the_number_of_1_bits import Solution


@pytest.mark.parametrize(
    "arr,expected",
    (
        ([0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 4, 8, 3, 5, 6, 7]),
        (
            [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],
            [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],
        ),
    ),
)
def test_solution(arr, expected):
    assert Solution().sortByBits(arr) == expected
