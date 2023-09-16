import pytest

from src.count_pairs_of_points_with_distance_k import Solution


@pytest.mark.parametrize(
    "coordinates,k,expected",
    (
        ([[1, 2], [4, 2], [1, 3], [5, 2]], 5, 2),
        ([[1, 3], [1, 3], [1, 3], [1, 3], [1, 3]], 0, 10),
        (
            [
                [27, 94],
                [61, 68],
                [47, 0],
                [100, 4],
                [127, 89],
                [61, 103],
                [26, 4],
                [51, 54],
                [91, 26],
                [98, 23],
                [80, 74],
                [19, 93],
            ],
            95,
            5,
        ),
    ),
)
def test_solution(coordinates, k, expected):
    assert Solution().countPairs(coordinates, k) == expected
