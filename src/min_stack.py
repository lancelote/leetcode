class MinStack:
    def __init__(self) -> None:
        self.val_stack: list[int] = []
        self.min_stack: list[int] = []

    def push(self, val: int) -> None:
        self.val_stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            smallest = min(self.min_stack[-1], val)
            self.min_stack.append(smallest)

    def pop(self) -> None:
        self.val_stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.val_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
