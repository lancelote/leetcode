import heapq


class LUPrefix:
    def __init__(self, n: int):
        self.n = n
        self.prefix = 0
        self.heap: list[int] = []

    def upload(self, video: int) -> None:
        heapq.heappush(self.heap, video)
        while self.heap and self.heap[0] == self.prefix + 1:
            heapq.heappop(self.heap)
            self.prefix += 1

    def longest(self) -> int:
        return self.prefix
