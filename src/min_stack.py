class MinStack:
    def __init__(self) -> None:
        self._val_stack: list[int] = []
        self._min_stack: list[int] = []

    def push(self, val: int) -> None:
        self._val_stack.append(val)

        if not self._min_stack:
            self._min_stack.append(val)
        else:
            new_min = min(self._min_stack[-1], val)
            self._min_stack.append(new_min)

    def pop(self) -> None:
        self._val_stack.pop()
        self._min_stack.pop()

    def top(self) -> int:
        return self._val_stack[-1]

    def getMin(self) -> int:
        return self._min_stack[-1]
