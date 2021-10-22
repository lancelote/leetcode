import pytest

from src.number_of_rectangles_that_can_form_the_largest_square import Solution


@pytest.mark.parametrize(
    "rectangles,expected_count",
    [
        ([[5, 8], [3, 9], [5, 12], [16, 5]], 3),
        ([[2, 3], [3, 7], [4, 3], [3, 7]], 3),
    ],
)
def test_solution(rectangles, expected_count):
    assert Solution().countGoodRectangles(rectangles) == expected_count
