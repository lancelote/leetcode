import pytest

from src.reverse_bits import Solution


@pytest.mark.parametrize(
    "n,expected",
    [
        (43261596, 964176192),
        (4294967293, 3221225471),
    ],
)
def test_solution(n, expected):
    assert Solution().reverseBits(n) == expected
