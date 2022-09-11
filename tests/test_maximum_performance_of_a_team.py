import pytest

from src.maximum_performance_of_a_team import Solution


@pytest.mark.parametrize(
    "n,speed,efficiency,k,expected_perf",
    [
        (6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 2, 60),
        (6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 3, 68),
        (6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 4, 72),
    ],
)
def test_solution(n, speed, efficiency, k, expected_perf):
    assert Solution().maxPerformance(n, speed, efficiency, k) == expected_perf
