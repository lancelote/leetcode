import pytest

from src.ones_and_zeroes import Solution


@pytest.mark.parametrize(
    "strs,m,n,expected",
    (
        (["10", "0001", "111001", "1", "0"], 5, 3, 4),
        (["10", "0", "1"], 1, 1, 2),
        (["10", "0001", "111001", "1", "0"], 4, 3, 3),
    ),
)
def test_solution(strs, m, n, expected):
    assert Solution().findMaxForm(strs, m, n) == expected
