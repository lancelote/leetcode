import pytest

from src.reordered_power_of_2 import Solution


@pytest.mark.parametrize(
    "n,expected",
    [
        (1, True),
        (10, False),
        (45, False),
        (55, False),
        (46, True),
    ],
)
def test_solution(n, expected):
    assert Solution().reorderedPowerOf2(n) == expected
