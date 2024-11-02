from src.utils.linked_list import ListNode


class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(next=head)

        prev = dummy
        curr = head

        while curr:
            if curr.next and curr.val == curr.next.val:
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next

                prev.next = curr.next
            else:
                assert prev.next
                prev = prev.next

            curr = curr.next

        return dummy.next
