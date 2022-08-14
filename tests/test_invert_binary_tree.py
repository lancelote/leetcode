import pytest

from src.invert_binary_tree import Solution
from src.utils.binary_tree import list_to_tree
from src.utils.binary_tree import tree_to_list


@pytest.mark.parametrize(
    "in_list,expected_out_list",
    [
        ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
        ([], []),
        ([2, 1, 3], [2, 3, 1]),
    ],
)
def test_solution(in_list, expected_out_list):
    in_tree = list_to_tree(in_list)
    result_tree = Solution().invertTree(in_tree)
    result_list = tree_to_list(result_tree)
    assert result_list == expected_out_list
