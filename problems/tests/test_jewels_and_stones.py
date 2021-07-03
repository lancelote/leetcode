import pytest
from src.jewels_and_stones import Solution


@pytest.mark.parametrize(
    "jewels,stones,num_of_jewels",
    [
        ("aA", "aAAbbbb", 3),
        ("z", "ZZ", 0),
    ],
)
def test_solution(jewels, stones, num_of_jewels):
    assert Solution().numJewelsInStones(jewels, stones) == num_of_jewels
