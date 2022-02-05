import pytest

from src.merge_k_sorted_lists import ListNode
from src.merge_k_sorted_lists import OptNode
from src.merge_k_sorted_lists import Solution


def equal(l1: OptNode, l2: OptNode) -> bool:
    while l1 and l2:
        if l1.val != l2.val:
            return False
        l1 = l1.next
        l2 = l2.next

    return (l1 is None) and (l2 is None)


@pytest.mark.parametrize(
    "l1,l2,expected",
    [
        (None, ListNode(1), False),
        (ListNode(1), None, False),
        (None, None, True),
        (ListNode(1), ListNode(2), False),
        (ListNode(1), ListNode(1), True),
        (ListNode(1, ListNode(2)), ListNode(1, ListNode(2)), True),
        (ListNode(1), ListNode(1, ListNode(2)), False),
        (ListNode(1, ListNode(2)), ListNode(1), False),
    ],
)
def test_equal(l1, l2, expected):
    assert equal(l1, l2) == expected


def to_linked(array: list[int]) -> OptNode:
    if not array:
        return None

    dummy_head = ListNode()
    tail = dummy_head

    for item in array:
        tail.next = ListNode(item)
        tail = tail.next

    return dummy_head.next


@pytest.mark.parametrize(
    "array,expected_head",
    [
        ([1, 2, 3], ListNode(1, ListNode(2, ListNode(3)))),
        ([], None),
    ],
)
def test_to_linked(array, expected_head):
    assert equal(to_linked(array), expected_head)


@pytest.mark.parametrize(
    "lists,expected_list",
    [
        ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
        ([], []),
        ([[]], []),
    ],
)
def test_solution(lists, expected_list):
    heads = [to_linked(x) for x in lists]
    expected_head = to_linked(expected_list)

    assert equal(Solution().mergeKLists(heads), expected_head)
