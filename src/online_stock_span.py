class StockSpanner:
    def __init__(self) -> None:
        self.stack: list[tuple[int, int]] = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            _, old_span = self.stack.pop()
            span += old_span
        self.stack.append((price, span))
        return span
