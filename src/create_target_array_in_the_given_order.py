from typing import List


class Solution:
    def createTargetArray(
        self, nums: List[int], index: List[int]
    ) -> List[int]:
        result: List[int] = []
        for i, num in zip(index, nums):
            result[i:i] = [num]
        return result
