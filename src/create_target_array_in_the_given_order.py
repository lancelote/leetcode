class Solution:
    def createTargetArray(
        self, nums: list[int], index: list[int]
    ) -> list[int]:
        result: list[int] = []
        for i, num in zip(index, nums):
            result[i:i] = [num]
        return result
