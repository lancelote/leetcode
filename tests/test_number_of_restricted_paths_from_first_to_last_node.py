import pytest

from src.number_of_restricted_paths_from_first_to_last_node import Solution


@pytest.mark.parametrize(
    "n,edges,expected",
    (
        (
            5,
            [
                [1, 2, 3],
                [1, 3, 3],
                [2, 3, 1],
                [1, 4, 2],
                [5, 2, 2],
                [3, 5, 1],
                [5, 4, 10],
            ],
            3,
        ),
        (
            7,
            [
                [1, 3, 1],
                [4, 1, 2],
                [7, 3, 4],
                [2, 5, 3],
                [5, 6, 1],
                [6, 7, 2],
                [7, 5, 3],
                [2, 6, 4],
            ],
            1,
        ),
    ),
)
def test_solution(n, edges, expected):
    assert Solution().countRestrictedPaths(n, edges) == expected
