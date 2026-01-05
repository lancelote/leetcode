import pytest

from src.delete_node_in_a_linked_list import Solution
from src.utils.linked_list import ListNode
from src.utils.linked_list import to_linked_list
from src.utils.linked_list import to_list


def find_by_value(node: ListNode | None, val: int) -> ListNode | None:
    while node is not None and node.val != val:
        node = node.next
    return node


@pytest.mark.parametrize(
    "head_list,node_val,expected_list",
    [
        ([4, 5, 1, 9], 5, [4, 1, 9]),
        ([4, 5, 1, 9], 1, [4, 5, 9]),
    ],
)
def test_solution(head_list, node_val, expected_list):
    head = to_linked_list(head_list)

    node = find_by_value(head, node_val)
    assert node

    Solution().deleteNode(node)
    assert to_list(head) == expected_list
