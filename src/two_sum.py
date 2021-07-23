class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        processed: dict[int, int] = {}

        for i, first in enumerate(nums):
            if (second := target - first) in processed:
                return [processed[second], i]
            processed[first] = i

        return []
