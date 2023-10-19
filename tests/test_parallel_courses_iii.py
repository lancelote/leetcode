import pytest

from src.parallel_courses_iii import Solution


@pytest.mark.parametrize(
    "n,relations,time,expected",
    (
        (3, [[1, 3], [2, 3]], [3, 2, 5], 8),
        (5, [[1, 5], [2, 5], [3, 5], [3, 4], [4, 5]], [1, 2, 3, 4, 5], 12),
    ),
)
def test_solution(n, relations, time, expected):
    assert Solution().minimumTime(n, relations, time) == expected
