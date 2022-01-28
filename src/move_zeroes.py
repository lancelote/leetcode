class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        # mutate
        left = 0
        for right, x in enumerate(nums):
            if x:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
