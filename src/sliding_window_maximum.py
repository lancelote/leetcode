from collections import deque
from typing import Deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        d: Deque[tuple[int, int]] = deque()
        result: list[int] = []

        for i in range(k):
            while d and d[-1][1] <= nums[i]:
                d.pop()

            d.append((i, nums[i]))

        result.append(d[0][1])

        for i in range(k, len(nums)):
            while d and d[0][0] <= (i - k):
                d.popleft()

            while d and d[-1][1] <= nums[i]:
                d.pop()

            d.append((i, nums[i]))
            result.append(d[0][1])

        return result
