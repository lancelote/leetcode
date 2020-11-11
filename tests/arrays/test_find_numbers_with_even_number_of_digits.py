import pytest

from src.arrays.find_numbers_with_even_number_of_digits import Solution


@pytest.mark.parametrize(
    "array, expected",
    [
        ([12, 345, 2, 6, 7896], 2),
        ([555, 901, 482, 1771], 1),
    ],
)
def test_basic_examples(array, expected):
    assert Solution().findNumbers(array) == expected
