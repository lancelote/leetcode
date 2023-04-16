class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0

        for x in nums:
            result ^= x

        return result
