import pytest

from src.binary_tree_right_side_view import Solution
from src.utils.binary_tree import list_to_tree


@pytest.mark.parametrize(
    "in_list,expected_view",
    (
        ([1, 2, 3, None, 5, None, 4], [1, 3, 4]),
        ([1, None, 3], [1, 3]),
        ([], []),
    ),
)
def test_solution(in_list, expected_view):
    root = list_to_tree(in_list)
    assert Solution().rightSideView(root) == expected_view
