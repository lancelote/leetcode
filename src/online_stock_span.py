class StockSpanner:
    def __init__(self) -> None:
        self.stack: list[tuple[int, int]] = []

    def next(self, price: int) -> int:
        count = 1

        while self.stack and price >= self.stack[-1][1]:
            old_count, _ = self.stack.pop()
            count += old_count

        self.stack.append((count, price))
        return count
