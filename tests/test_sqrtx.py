import pytest

from src.sqrtx import Solution


@pytest.mark.parametrize(
    "x,expected_root",
    [
        (4, 2),
        (8, 2),
        (1, 1),
    ],
)
def test_solution(x, expected_root):
    assert Solution().mySqrt(x) == expected_root
