import pytest

from src.add_digits import Solution


@pytest.mark.parametrize(
    "num,expected",
    [
        (38, 2),
        (0, 0),
    ],
)
def test_solution(num, expected):
    assert Solution().addDigits(num) == expected
