import pytest

from src.palindrome_linked_list import equal
from src.palindrome_linked_list import reverse
from src.palindrome_linked_list import Solution
from src.utils.linked_list import ListNode
from src.utils.linked_list import to_linked_list
from src.utils.linked_list import to_list


@pytest.mark.parametrize(
    "head1,head2,expected",
    [
        (None, None, True),
        (ListNode(1), None, False),
        (None, ListNode(2), False),
        (ListNode(1), ListNode(2), False),
        (ListNode(1), ListNode(1), True),
        (ListNode(1, ListNode(2)), ListNode(1, ListNode(2)), True),
        (ListNode(1, ListNode(3)), ListNode(1, ListNode(2)), False),
        (ListNode(1, ListNode(2)), ListNode(3, ListNode(2)), False),
    ],
)
def test_equal(head1, head2, expected):
    assert equal(head1, head2) is expected


@pytest.mark.parametrize(
    "in_list,out_list",
    [
        ([], []),
        ([1], [1]),
        ([1, 2], [2, 1]),
        ([1, 2, 3], [3, 2, 1]),
    ],
)
def test_reverse(in_list, out_list):
    head = to_linked_list(in_list)
    result = reverse(head)
    assert to_list(result) == out_list


@pytest.mark.parametrize(
    "in_list,expected",
    [
        ([1, 2, 2, 1], True),
        ([1, 2, 1], True),
        ([1], True),
        ([1, 2], False),
        ([1, 2, 2], False),
    ],
)
def test_solution(in_list, expected):
    head = to_linked_list(in_list)
    assert Solution().isPalindrome(head) is expected
