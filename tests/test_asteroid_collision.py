import pytest

from src.asteroid_collision import Solution


@pytest.mark.parametrize(
    "asteroids,expected",
    (
        ([5, 10, -5], [5, 10]),
        ([8, -8], []),
        ([10, 2, -5], [10]),
        ([-2, -1, 1, 2], [-2, -1, 1, 2]),
        ([-2, -2, 1, -2], [-2, -2, -2]),
    ),
)
def test_solution(asteroids, expected):
    assert Solution().asteroidCollision(asteroids) == expected
