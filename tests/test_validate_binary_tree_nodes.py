import pytest

from src.validate_binary_tree_nodes import Solution


@pytest.mark.parametrize(
    "n,left_child,right_child,expected",
    (
        (4, [1, -1, 3, -1], [2, -1, -1, -1], True),
        (4, [1, -1, 3, -1], [2, 3, -1, -1], False),
        (2, [1, 0], [-1, -1], False),
    ),
)
def test_solution(n, left_child, right_child, expected):
    assert (
        Solution().validateBinaryTreeNodes(n, left_child, right_child)
        == expected
    )
