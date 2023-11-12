import pytest

from src.bus_routes import Solution


@pytest.mark.parametrize(
    "routes,source,target,expected",
    (
        ([[1, 2, 7], [3, 6, 7]], 1, 6, 2),
        ([[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]], 15, 12, -1),
        ([[1, 7], [3, 5]], 5, 5, 0),
        (
            [
                [16, 25, 29, 35, 42],
                [32],
                [1],
                [1, 2, 5, 17, 22, 34, 38, 41, 44],
                [1, 16, 23, 24, 32, 36, 38, 45],
                [9, 11, 43],
                [5, 10, 15, 22, 27, 38],
                [7, 8, 14, 19, 22, 23, 25, 26, 27],
                [3, 8, 24, 29, 47, 48],
                [4, 16, 18, 25, 36, 41],
            ],
            17,
            38,
            1,
        ),
    ),
)
def test_solution(routes, source, target, expected):
    assert Solution().numBusesToDestination(routes, source, target) == expected
