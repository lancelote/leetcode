class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        sorted_nums = sorted(nums)
        counts = {}

        for i, num in enumerate(sorted_nums):
            if num not in counts:
                counts[num] = i

        return [counts[num] for num in nums]
