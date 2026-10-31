class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        n = len(nums)
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = left + (right - left) // 2

            if middle < n - 1 and nums[middle] < nums[middle + 1]:
                left = middle + 1
            elif middle > 0 and nums[middle] < nums[middle - 1]:
                right = middle - 1
            else:
                return middle

        raise ValueError("answer not found")
