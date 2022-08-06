from src.utils.linked_list import ListNode
from src.utils.linked_list import to_linked_list
from src.utils.linked_list import to_list


def test_to_linked_list():
    head = to_linked_list([1, 2])

    assert isinstance(head, ListNode)
    assert head.val == 1

    assert isinstance(head.next, ListNode)
    assert head.next.val == 2

    assert head.next.next is None


def test_to_list():
    head = ListNode(1, ListNode(2, ListNode(3, None)))
    assert to_list(head) == [1, 2, 3]
