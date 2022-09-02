import pytest

from src.average_of_levels_in_binary_tree import Solution
from src.utils.binary_tree import list_to_tree


@pytest.mark.parametrize(
    "in_list,expected_averages",
    [
        ([3, 9, 20, None, None, 15, 7], [3.00000, 14.50000, 11.00000]),
        ([3, 9, 20, 15, 7], [3.00000, 14.50000, 11.00000]),
    ],
)
def test_solution(in_list, expected_averages):
    root = list_to_tree(in_list)
    assert Solution().averageOfLevels(root) == expected_averages
