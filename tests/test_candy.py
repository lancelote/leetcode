import pytest

from src.candy import Solution


@pytest.mark.parametrize(
    "ratings,expected",
    (
        ([1, 0, 2], 5),
        ([1, 2, 2], 4),
        ([1, 3, 4, 5, 2], 11),
    ),
)
def test_solution(ratings, expected):
    assert Solution().candy(ratings) == expected
