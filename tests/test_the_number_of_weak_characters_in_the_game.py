import pytest

from src.the_number_of_weak_characters_in_the_game import Solution


@pytest.mark.parametrize(
    "properties,weak_count",
    [
        ([[5, 5], [6, 3], [3, 6]], 0),
        ([[2, 2], [3, 3]], 1),
        ([[1, 5], [10, 4], [4, 3]], 1),
    ],
)
def test_solution(properties, weak_count):
    assert Solution().numberOfWeakCharacters(properties) == weak_count
