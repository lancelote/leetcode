from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total = 0
        result = []

        for num in nums:
            total += num
            result.append(total)

        return result
