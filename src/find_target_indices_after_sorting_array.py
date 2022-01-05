class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        less_than = 0
        equal = 0
        for num in nums:
            if num < target:
                less_than += 1
            elif num == target:
                equal += 1
        return list(range(less_than, less_than + equal))
