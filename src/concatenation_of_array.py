class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [0] * (2 * n)

        for i in range(2 * n):
            result[i] = nums[i % n]

        return result
