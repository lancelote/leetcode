import pytest

from src.maximum_number_of_coins_you_can_get import Solution


@pytest.mark.parametrize(
    "piles,expected",
    (
        ([2, 4, 1, 2, 7, 8], 9),
        ([2, 4, 5], 4),
        ([9, 8, 7, 6, 5, 1, 2, 3, 4], 18),
    ),
)
def test_solution(piles, expected):
    assert Solution().maxCoins(piles) == expected
