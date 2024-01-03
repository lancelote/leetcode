import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        h: list[int] = []

        for x in nums:
            heapq.heappush(h, x)
            if len(h) > k:
                heapq.heappop(h)

        return h[0]
