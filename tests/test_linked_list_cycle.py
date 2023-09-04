from src.linked_list_cycle import Solution
from src.utils.linked_list import ListNode


def test_solution_true():
    first = ListNode(1)
    second = ListNode(2)
    first.next = second
    second.next = first

    assert Solution().hasCycle(first)


def test_solution_false():
    head = ListNode(1, ListNode(2))

    assert Solution().hasCycle(head) is False


def test_empty():
    assert Solution().hasCycle(None) is False
