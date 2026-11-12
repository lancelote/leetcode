import pytest

from src.find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance import (
    Solution,
)


@pytest.mark.parametrize(
    "n,edges,distance_threshold,expected",
    (
        (2, [[0, 1, 2]], 2, 1),
        (4, [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], 4, 3),
        (
            5,
            [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]],
            2,
            0,
        ),
    ),
)
def test_solution(n, edges, distance_threshold, expected):
    assert Solution().findTheCity(n, edges, distance_threshold) == expected
