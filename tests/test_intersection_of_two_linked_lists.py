from src.intersection_of_two_linked_lists import Solution
from src.utils.linked_list import ListNode


def test_solution():
    common = ListNode(8, ListNode(4, ListNode(5)))
    head_a = ListNode(4, ListNode(1, common))
    head_b = ListNode(5, ListNode(6, ListNode(1, common)))

    assert Solution().getIntersectionNode(head_a, head_b) == common
