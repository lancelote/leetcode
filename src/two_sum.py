class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        compliments: dict[int, int] = {}

        for i, x in enumerate(nums):
            compliment = target - x
            if compliment in compliments:
                return [compliments[compliment], i]
            compliments[x] = i

        raise ValueError("solution not found")
