import pytest

from src.combination_sum_iii import Solution


@pytest.mark.parametrize(
    "k,n,expected",
    (
        (3, 7, [[1, 2, 4]]),
        (3, 9, [[1, 2, 6], [1, 3, 5], [2, 3, 4]]),
        (4, 1, []),
    ),
)
def test_solution(k, n, expected):
    assert Solution().combinationSum3(k, n) == expected
