import pytest

from src.subtree_of_another_tree import Solution
from src.utils.binary_tree import list_to_tree


@pytest.mark.parametrize(
    "root_list,sub_root_list,expected",
    [
        ([1], [2], False),
        ([1], [1, 2], False),
        ([1], [1, None, 2], False),
        ([3, 4, 5, 1, 2], [4, 1, 2], True),
        ([3, 4, 5, 1, 2, None, None, None, None, 0], [4, 1, 2], False),
        (
            [
                1,
                None,
                1,
                None,
                1,
                None,
                1,
                None,
                1,
                None,
                1,
                None,
                1,
                None,
                1,
                None,
                1,
                None,
                1,
                None,
                1,
                2,
            ],
            [1, None, 1, None, 1, None, 1, None, 1, None, 1, 2],
            True,
        ),
    ],
)
def test_solution(root_list, sub_root_list, expected):
    root = list_to_tree(root_list)
    sub_root = list_to_tree(sub_root_list)
    assert Solution().isSubtree(root, sub_root) == expected
