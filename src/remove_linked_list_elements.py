from src.utils.linked_list import ListNode


class Solution:
    def removeElements(
        self, head: ListNode | None, val: int
    ) -> ListNode | None:
        dummy = ListNode(next=head)

        prev = dummy
        current = head
        while current is not None:
            if current.val == val:
                current = current.next
            else:
                prev.next = current
                prev, current = current, current.next

        prev.next = None
        return dummy.next
