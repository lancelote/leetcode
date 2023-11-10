import pytest

from src.restore_the_array_from_adjacent_pairs import Solution


@pytest.mark.parametrize(
    "adjacent_pairs,expected",
    (
        ([[2, 1], [3, 4], [3, 2]], [1, 2, 3, 4]),
        ([[4, -2], [1, 4], [-3, 1]], [-2, 4, 1, -3]),
        ([[100000, -100000]], [-100000, 100000]),
    ),
)
def test_solution(adjacent_pairs, expected):
    assert Solution().restoreArray(adjacent_pairs) == expected
