from src.utils.linked_list import ListNode


class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(-1, next=head)

        slow = fast = dummy

        while slow and fast and fast.next and fast.next.next:
            slow = slow.next  # type: ignore
            fast = fast.next.next

        if slow.next:
            slow.next = slow.next.next

        return dummy.next
