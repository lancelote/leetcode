class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        compliment: dict[int, int] = {}

        for i, x in enumerate(nums):
            if x in compliment:
                return [compliment[x], i]
            compliment[target - x] = i

        raise ValueError("no answer found")
