import pytest

from src.count_nodes_equal_to_average_of_subtree import Solution
from src.utils.binary_tree import list_to_tree


@pytest.mark.parametrize(
    "in_list,expected",
    (
        ([4, 8, 5, 0, 1, None, 6], 5),
        ([1], 1),
    ),
)
def test_solution(in_list, expected):
    root = list_to_tree(in_list)
    assert Solution().averageOfSubtree(root) == expected
