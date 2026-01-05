import pytest

from src.count_good_nodes_in_binary_tree import Solution
from src.utils.binary_tree import list_to_tree


@pytest.mark.parametrize(
    "in_list,expected_good",
    [
        ([3, 1, 4, 3, None, 1, 5], 4),
        ([3, 3, None, 4, 2], 3),
        ([1], 1),
    ],
)
def test_solution(in_list, expected_good):
    head = list_to_tree(in_list)

    assert head is not None
    assert Solution().goodNodes(head) == expected_good
