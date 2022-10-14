from src.utils.linked_list import ListNode


class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return None

        dummy = ListNode(next=head)
        slow, fast = dummy, dummy

        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next
        return dummy.next
