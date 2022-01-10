class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        largest = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                largest = max((nums[i] - 1) * (nums[j] - 1), largest)

        return largest
