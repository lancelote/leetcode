import heapq


class Solution:
    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        pairs = [(x2, x1) for x1, x2 in zip(nums1, nums2)]
        pairs.sort(reverse=True)

        h: list[int] = []
        total = 0
        result = 0

        for x2, x1 in pairs:
            total += x1
            heapq.heappush(h, x1)

            if len(h) > k:
                total -= heapq.heappop(h)

            if len(h) == k:
                result = max(result, total * x2)

        return result
