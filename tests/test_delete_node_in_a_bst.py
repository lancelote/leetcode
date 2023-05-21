import pytest

from src.delete_node_in_a_bst import Solution
from src.utils.binary_search_tree import list_to_tree
from src.utils.binary_search_tree import tree_to_list


@pytest.mark.parametrize(
    "in_list,key,out_list",
    (
        ([5, 3, 6, 2, 4, None, 7], 3, [5, 4, 6, 2, 7]),
        ([5, 3, 6, 2, 4, None, 7], 0, [5, 3, 6, 2, 4, 7]),
        ([], 0, []),
    ),
)
def test_solution(in_list, key, out_list):
    in_tree = list_to_tree(in_list)
    out_tree = Solution().deleteNode(in_tree, key)
    assert tree_to_list(out_tree) == out_list
