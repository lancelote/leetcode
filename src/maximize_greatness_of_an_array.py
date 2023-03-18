class Solution:
    def maximizeGreatness(self, nums: list[int]) -> int:
        sorted_nums = sorted(nums, reverse=True)
        i = 0

        for x in sorted_nums:
            if sorted_nums[i] > x:
                i += 1

        return i
