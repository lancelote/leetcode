import heapq


class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        heap: list[tuple[int, int]] = []

        for item in arr:
            diff = abs(x - item)
            heapq.heappush(heap, (-diff, -item))
            if len(heap) > k:
                heapq.heappop(heap)

        return sorted(-item for _, item in heap)
