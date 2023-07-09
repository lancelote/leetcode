import heapq as h


class RecentCounter:
    def __init__(self) -> None:
        self.heap: list[int] = []

    def ping(self, t: int) -> int:
        while self.heap and self.heap[0] < t - 3000:
            h.heappop(self.heap)
        h.heappush(self.heap, t)
        return len(self.heap)
