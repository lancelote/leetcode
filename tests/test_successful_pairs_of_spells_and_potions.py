import pytest

from src.successful_pairs_of_spells_and_potions import Solution


@pytest.mark.parametrize(
    "spells,potions,success,expected",
    (
        ([5, 1, 3], [1, 2, 3, 4, 5], 7, [4, 0, 3]),
        ([3, 1, 2], [8, 5, 8], 16, [2, 0, 2]),
    ),
)
def test_solution(spells, potions, success, expected):
    assert Solution().successfulPairs(spells, potions, success) == expected
