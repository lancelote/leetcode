import pytest

from src.count_zero_request_servers import Solution


@pytest.mark.parametrize(
    "n,logs,x,queries,expected",
    (
        (3, [[1, 3], [2, 6], [1, 5]], 5, [10, 11], [1, 2]),
        (3, [[2, 4], [2, 1], [1, 2], [3, 1]], 2, [3, 4], [0, 1]),
        (
            3,
            [[1, 35], [1, 32], [1, 11], [1, 39], [2, 29]],
            8,
            [38, 30, 23, 33, 15, 31, 34, 22, 11, 14],
            [2, 2, 3, 1, 2, 2, 1, 3, 2, 2],
        ),
    ),
)
def test_solution(n, logs, x, queries, expected):
    assert Solution().countServers(n, logs, x, queries) == expected
