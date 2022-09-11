import heapq


class MedianFinder:
    def __init__(self) -> None:
        self.small_heap: list[int] = []  # max heap
        self.large_heap: list[int] = []  # min heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small_heap, -num)

        if (
            self.small_heap
            and self.large_heap
            and -self.small_heap[0] > self.large_heap[0]
        ):
            pop_val = -heapq.heappop(self.small_heap)
            heapq.heappush(self.large_heap, pop_val)

        if len(self.small_heap) - len(self.large_heap) > 1:
            pop_val = -heapq.heappop(self.small_heap)
            heapq.heappush(self.large_heap, pop_val)

        if len(self.large_heap) - len(self.small_heap) > 1:
            pop_val = heapq.heappop(self.large_heap)
            heapq.heappush(self.small_heap, -pop_val)

    def findMedian(self) -> float:
        if len(self.small_heap) > len(self.large_heap):
            return -self.small_heap[0]
        elif len(self.small_heap) < len(self.large_heap):
            return self.large_heap[0]
        else:
            return (-self.small_heap[0] + self.large_heap[0]) / 2
