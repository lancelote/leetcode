from src.utils.linked_list import ListNode


def get_length(head: ListNode | None) -> int:
    if head is None:
        return 0

    length = 0

    while head is not None:
        length += 1
        head = head.next

    return length


class Solution:
    def splitListToParts(
        self, head: ListNode | None, k: int
    ) -> list[ListNode | None]:
        length = get_length(head)
        result = [ListNode(-1) for _ in range(k)]  # dummies

        each = length // k
        extra = length % k

        for i in range(k):
            current: ListNode | None = result[i]

            for _ in range(each):
                assert current and head

                current.next = head
                current = current.next
                head = head.next

            if extra:
                assert current and head

                current.next = head
                current = current.next
                head = head.next

                extra -= 1

            assert current
            current.next = None

        return [x.next for x in result]  # unpack dummies
