class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [1] * n

        prefix = 1

        for i, x in enumerate(nums):
            result[i] = prefix
            prefix *= x

        postfix = 1

        for i in range(n - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result
