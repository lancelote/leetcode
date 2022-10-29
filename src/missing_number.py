class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        result = len(nums)

        for i in range(len(nums)):
            result ^= nums[i] ^ i

        return result
