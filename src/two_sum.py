class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen: dict[int, int] = {}

        for i, x in enumerate(nums):
            compliment = target - x
            if compliment in seen:
                return [seen[compliment], i]
            seen[x] = i

        raise ValueError
