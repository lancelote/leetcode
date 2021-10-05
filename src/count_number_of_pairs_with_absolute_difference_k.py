from collections import defaultdict
from typing import DefaultDict


class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        result = 0
        seen: DefaultDict[int, int] = defaultdict(int)

        for num in nums:
            result += seen[num - k] + seen[num + k]
            seen[num] += 1

        return result
