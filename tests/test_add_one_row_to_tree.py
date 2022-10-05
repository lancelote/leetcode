import pytest

from src.add_one_row_to_tree import Solution
from src.utils.binary_tree import list_to_tree
from src.utils.binary_tree import tree_to_list


@pytest.mark.parametrize(
    "in_list,val,depth,out_list",
    [
        ([4, 2, 6, 3, 1, 5], 1, 2, [4, 1, 1, 2, None, None, 6, 3, 1, 5]),
        ([4, 2, None, 3, 1], 1, 3, [4, 2, None, 1, 1, 3, None, None, 1]),
    ],
)
def test_solution(in_list, val, depth, out_list):
    root = list_to_tree(in_list)
    result = Solution().addOneRow(root, val, depth)
    result_list = tree_to_list(result)
    assert result_list == out_list
