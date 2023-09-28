class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[left] % 2 != 0:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            if nums[left] % 2 == 0:
                left += 1

        return nums
