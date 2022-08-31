import pytest

from src.pacific_atlantic_water_flow import Solution


@pytest.mark.parametrize(
    "heights,expected_points",
    [
        (
            [
                [1, 2, 2, 3, 5],
                [3, 2, 3, 4, 4],
                [2, 4, 5, 3, 1],
                [6, 7, 1, 4, 5],
                [5, 1, 1, 2, 4],
            ],
            [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]],
        ),
        ([[1]], [[0, 0]]),
        (
            [[1, 1], [1, 1], [1, 1]],
            [[0, 1], [2, 1], [0, 0], [1, 1], [2, 0], [1, 0]],
        ),
        (
            [[1, 2, 3], [8, 9, 4], [7, 6, 5]],
            [[0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]],
        ),
    ],
)
def test_solution(heights, expected_points):
    result = Solution().pacificAtlantic(heights)
    assert {(r, c) for r, c in result} == {(r, c) for r, c in expected_points}
