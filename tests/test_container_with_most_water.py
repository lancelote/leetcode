import pytest

from src.container_with_most_water import Solution


@pytest.mark.parametrize(
    "height,expected",
    [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
    ],
)
def test_solution(height, expected):
    assert Solution().maxArea(height) == expected
