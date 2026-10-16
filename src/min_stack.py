class MinStack:
    def __init__(self) -> None:
        self.val_stack: list[int] = []
        self.min_stack: list[int] = []

    def push(self, value: int) -> None:
        self.val_stack.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self) -> None:
        if self.min_stack[-1] == self.val_stack[-1]:
            self.min_stack.pop()
        self.val_stack.pop()

    def top(self) -> int:
        return self.val_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
