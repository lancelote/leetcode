import pytest

from src.remove_nth_node_from_end_of_list import ListNode
from src.remove_nth_node_from_end_of_list import OptNode
from src.remove_nth_node_from_end_of_list import Solution


def to_linked(array: list[int]) -> OptNode:
    if not array:
        return None

    dummy = ListNode()
    tail = dummy

    for x in array:
        tail.next = ListNode(x)
        tail = tail.next

    return dummy.next


def equal(l1: OptNode, l2: OptNode) -> bool:
    while l1 and l2:
        if l1.val != l2.val:
            return False
        l1 = l1.next
        l2 = l2.next

    return l1 is None and l2 is None


@pytest.mark.parametrize(
    "head_array,n,expected_array",
    [
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
        ([1], 1, []),
        ([1, 2], 1, [1]),
    ],
)
def test_solution(head_array, n, expected_array):
    head = to_linked(head_array)
    expected = to_linked(expected_array)

    assert equal(Solution().removeNthFromEnd(head, n), expected)
