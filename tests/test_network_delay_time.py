import pytest

from src.network_delay_time import Solution


@pytest.mark.parametrize(
    "times,n,k,expected",
    (
        ([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2, 2),
        ([[1, 2, 1]], 2, 1, 1),
        ([[1, 2, 1]], 2, 2, -1),
    ),
)
def test_solution(times, n, k, expected):
    assert Solution().networkDelayTime(times, n, k) == expected
