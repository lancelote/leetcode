import heapq


class Solution:
    def largestSumAfterKNegations(self, nums: list[int], k: int) -> int:
        h = nums[::]
        heapq.heapify(h)

        for _ in range(k):
            smallest = heapq.heappop(h)
            if smallest == 0:
                break
            heapq.heappush(h, -smallest)

        return sum(h)
