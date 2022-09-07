import pytest

from src.construct_string_from_binary_tree import Solution
from src.utils.binary_tree import list_to_tree


@pytest.mark.parametrize(
    "in_list,expected_output",
    [
        ([1, 2, 3, 4], "1(2(4))(3)"),
        ([1, 2, 3, None, 4], "1(2()(4))(3)"),
        ([1], "1"),
    ],
)
def test_solution(in_list, expected_output):
    root = list_to_tree(in_list)
    assert Solution().tree2str(root) == expected_output
