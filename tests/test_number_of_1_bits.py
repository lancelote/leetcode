import pytest

from src.number_of_1_bits import Solution


@pytest.mark.parametrize(
    "n,expected",
    [
        (11, 3),
        (128, 1),
        (4294967293, 31),
    ],
)
def test_solution(n, expected):
    assert Solution().hammingWeight(n) == expected
