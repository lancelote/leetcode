class Solution:
    def isGood(self, nums: list[int]) -> bool:
        if len(nums) < 2:
            return False

        sorted_nums = sorted(nums)

        for i in range(len(nums) - 2):
            if sorted_nums[i] + 1 != sorted_nums[i + 1]:
                return False

        return sorted_nums[-1] == sorted_nums[-2] == len(nums) - 1
