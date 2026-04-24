import pytest

from src.closest_binary_search_tree_value import Solution
from src.utils.binary_search_tree import list_to_tree


@pytest.mark.parametrize(
    "in_list,target,expected",
    (
        ([4, 2, 5, 1, 3], 3.714286, 4),
        ([1], 4.428571, 1),
    ),
)
def test_solution(in_list, target, expected):
    root = list_to_tree(in_list)
    assert Solution().closestValue(root, target) == expected
