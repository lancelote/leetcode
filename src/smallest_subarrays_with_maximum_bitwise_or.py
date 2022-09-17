class Solution:
    def smallestSubarrays(self, nums: list[int]) -> list[int]:
        result: list[int] = [0] * len(nums)
        last = [0] * 32

        for i in range(len(nums) - 1, -1, -1):
            for j in range(32):
                if nums[i] & 1 << j:
                    last[j] = i
            result[i] = max(1, max(last) - i + 1)

        return result
