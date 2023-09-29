class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        if len(nums) == 1:
            return True

        decreasing = 0
        increasing = 0

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                decreasing += 1
            elif nums[i] < nums[i + 1]:
                increasing += 1

            if decreasing and increasing:
                return False

        return True
