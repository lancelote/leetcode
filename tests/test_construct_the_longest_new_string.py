import pytest

from sample2 import Solution


@pytest.mark.parametrize(
    "x,y,z,expected",
    (
        (2, 5, 1, 12),
        (3, 2, 2, 14),
        (1, 0, 0, 2),
        (3, 0, 0, 2),
        (1, 1, 1, 6),
        (2, 1, 0, 6),
        (2, 2, 0, 8),
        (1, 5, 0, 6),
        (1, 5, 1, 8),
    ),
)
def test_solution(x, y, z, expected):
    assert Solution().longestString(x, y, z) == expected
