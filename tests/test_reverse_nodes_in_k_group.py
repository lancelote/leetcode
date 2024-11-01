import pytest

from src.reverse_nodes_in_k_group import Solution
from src.utils.linked_list import to_linked_list
from src.utils.linked_list import to_list


@pytest.mark.parametrize(
    "in_list,k,out_list",
    [
        ([1, 2, 3, 4, 5], 2, [2, 1, 4, 3, 5]),
        ([1, 2, 3, 4, 5], 3, [3, 2, 1, 4, 5]),
        ([1, 2], 2, [2, 1]),
    ],
)
def test_solution(in_list, k, out_list):
    head = to_linked_list(in_list)
    modified = Solution().reverseKGroup(head, k)
    assert to_list(modified) == out_list
