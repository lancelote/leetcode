import pytest

from src.kids_with_the_greatest_number_of_candies import Solution


@pytest.mark.parametrize(
    "kids,extra,expected",
    [
        ([2, 3, 5, 1, 3], 3, [True, True, True, False, True]),
        ([4, 2, 1, 1, 2], 1, [True, False, False, False, False]),
        ([12, 1, 12], 10, [True, False, True]),
    ],
)
def test_solution(kids, extra, expected):
    assert Solution().kidsWithCandies(kids, extra) == expected
