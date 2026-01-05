from src.utils.linked_list import ListNode


def reverse(head: ListNode | None) -> ListNode | None:
    previous = None

    while head:
        tmp = head.next
        head.next = previous
        previous = head
        head = tmp

    return previous


def equal(head1: ListNode | None, head2: ListNode | None) -> bool:
    while head1 and head2:
        if head1.val != head2.val:
            return False
        head1 = head1.next
        head2 = head2.next
    return not head1 and not head2


class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        if not head:
            return True

        slow, fast = head, head

        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        if not fast.next:
            second_part = slow
        else:
            assert slow is not None

            second_part = slow.next
            slow.next = None

        second_reversed = reverse(second_part)
        return equal(head, second_reversed)
