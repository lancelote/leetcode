import pytest

from src.number_of_ways_to_arrive_at_destination import Solution


@pytest.mark.parametrize(
    "n,roads,expected",
    (
        (
            7,
            [
                [0, 6, 7],
                [0, 1, 2],
                [1, 2, 3],
                [1, 3, 3],
                [6, 3, 3],
                [3, 5, 1],
                [6, 5, 1],
                [2, 5, 1],
                [0, 4, 5],
                [4, 6, 2],
            ],
            4,
        ),
        (2, [[1, 0, 10]], 1),
    ),
)
def test_solution(n, roads, expected):
    assert Solution().countPaths(n, roads) == expected
