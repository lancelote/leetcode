import pytest

from src.utils.linked_list import is_equal
from src.utils.linked_list import ListNode
from src.utils.linked_list import to_linked_list
from src.utils.linked_list import to_list


def test_to_linked_list_1():
    head = to_linked_list([1, 2])

    assert isinstance(head, ListNode)
    assert head.val == 1

    assert isinstance(head.next, ListNode)
    assert head.next.val == 2

    assert head.next.next is None


@pytest.mark.parametrize(
    "lst,expected_head",
    [
        ([1, 2, 3], ListNode(1, ListNode(2, ListNode(3)))),
        ([], None),
    ],
)
def test_to_linked_list_2(lst, expected_head):
    assert is_equal(to_linked_list(lst), expected_head)


def test_to_list():
    head = ListNode(1, ListNode(2, ListNode(3, None)))
    assert to_list(head) == [1, 2, 3]


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
def test_is_equal(l1, l2, expected):
    assert is_equal(l1, l2) is expected
