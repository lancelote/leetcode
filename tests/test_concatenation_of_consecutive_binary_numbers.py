import pytest

from src.concatenation_of_consecutive_binary_numbers import Solution


@pytest.mark.parametrize(
    "n,expected",
    [
        (1, 1),
        (3, 27),
        (12, 505379714),
    ],
)
def test_solution(n, expected):
    assert Solution().concatenatedBinary(n) == expected
