class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [1] * n

        tmp = 1
        for i in range(1, n):
            tmp *= nums[i - 1]
            result[i] *= tmp

        tmp = 1
        for i in range(n - 2, -1, -1):
            tmp *= nums[i + 1]
            result[i] *= tmp

        return result
