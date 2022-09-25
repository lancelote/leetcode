from __future__ import annotations


class ListNode:
    def __init__(
        self,
        val: int = -1,
        prv: ListNode | None = None,
        nxt: ListNode | None = None,
    ) -> None:
        self.val = val
        self.prv = prv
        self.nxt = nxt

    def __repr__(self) -> str:
        return f"ListNode({self.val})"


class MyCircularQueue:
    def __init__(self, k: int):
        self.capacity = k
        self.left = ListNode()
        self.right = ListNode(prv=self.left)
        self.left.nxt = self.right

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        new_node = ListNode(value, self.right.prv, self.right)

        assert self.right.prv
        self.right.prv.nxt = new_node
        self.right.prv = new_node

        self.capacity -= 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        assert self.left.nxt
        self.left.nxt = self.left.nxt.nxt

        assert self.left.nxt
        self.left.nxt.prv = self.left

        self.capacity += 1
        return True

    def Front(self) -> int:
        assert self.left.nxt
        return self.left.nxt.val

    def Rear(self) -> int:
        assert self.right.prv
        return self.right.prv.val

    def isEmpty(self) -> bool:
        return self.left.nxt is self.right

    def isFull(self) -> bool:
        return self.capacity == 0
