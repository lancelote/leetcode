import pytest

from src.valid_perfect_square import Solution


@pytest.mark.parametrize(
    "num,expected",
    (
        (16, True),
        (14, False),
        (1, True),
        (4, True),
    ),
)
def test_solution(num, expected):
    assert Solution().isPerfectSquare(num) is expected
