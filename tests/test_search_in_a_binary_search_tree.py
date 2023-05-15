import pytest

from src.search_in_a_binary_search_tree import Solution
from src.utils.binary_search_tree import list_to_tree
from src.utils.binary_search_tree import tree_to_list


@pytest.mark.parametrize(
    "in_list,val,out_list",
    (
        ([4, 2, 7, 1, 3], 2, [2, 1, 3]),
        ([4, 2, 7, 1, 3], 5, []),
    ),
)
def test_solution(in_list, val, out_list):
    root = list_to_tree(in_list)
    out_tree = Solution().searchBST(root, val)
    assert tree_to_list(out_tree) == out_list
