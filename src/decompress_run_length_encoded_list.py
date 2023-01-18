class Solution:
    def decompressRLElist(self, nums: list[int]) -> list[int]:
        result = []

        for i in range(0, len(nums), 2):
            freq = nums[i]
            val = nums[i + 1]
            result.extend([val] * freq)

        return result
