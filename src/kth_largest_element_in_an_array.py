import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap: list[int] = []

        for x in nums:
            heapq.heappush(heap, x)
            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]
