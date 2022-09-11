import pytest

from src.last_stone_weight import Solution


@pytest.mark.parametrize(
    "stones,expected_last",
    [
        ([2, 7, 4, 1, 8, 1], 1),
        ([1], 1),
    ],
)
def test_solution(stones, expected_last):
    assert Solution().lastStoneWeight(stones) == expected_last
