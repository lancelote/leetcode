import typing as t
from collections import deque


class MyStack:
    def __init__(self) -> None:
        self.deque: t.Deque[int] = deque()

    def push(self, x: int) -> None:
        self.deque.append(x)

    def pop(self) -> int:
        for _ in range(len(self.deque) - 1):
            self.deque.append(self.deque.popleft())
        return self.deque.popleft()

    def top(self) -> int:
        return self.deque[-1]

    def empty(self) -> bool:
        return not len(self.deque)
