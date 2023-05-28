class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        slow = 0

        for fast, x in enumerate(nums):
            if x != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
