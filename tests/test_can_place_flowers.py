import pytest

from src.can_place_flowers import Solution


@pytest.mark.parametrize(
    "flowerbed,n,expected",
    (
        ([1, 0, 0, 0, 1], 1, True),
        ([1, 0, 0, 0, 1], 2, False),
        ([1, 0, 0, 0, 0, 1], 2, False),
        ([0], 1, True),
    ),
)
def test_solution(flowerbed, n, expected):
    assert Solution().canPlaceFlowers(flowerbed, n) is expected
