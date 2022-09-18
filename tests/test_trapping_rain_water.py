import pytest

from src.trapping_rain_water import Solution


@pytest.mark.parametrize(
    "height,expected_water",
    [
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([4, 2, 0, 3, 2, 5], 9),
    ],
)
def test_solution(height, expected_water):
    assert Solution().trap(height) == expected_water
