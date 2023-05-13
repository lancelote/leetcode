import pytest

from src.koko_eating_bananas import Solution


@pytest.mark.parametrize(
    "k,piles,expected",
    (
        (6, [3, 6, 7, 11], 6),
        (11, [3, 6, 7, 11], 4),
    ),
)
def test_will_take(k, piles, expected):
    assert Solution().will_take(k, piles) == expected


@pytest.mark.parametrize(
    "piles,h,expected",
    (
        ([3, 6, 7, 11], 8, 4),
        ([30, 11, 23, 4, 20], 5, 30),
        ([30, 11, 23, 4, 20], 6, 23),
    ),
)
def test_solution(piles, h, expected):
    assert Solution().minEatingSpeed(piles, h) == expected
