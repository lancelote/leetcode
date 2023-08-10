class Solution:
    def rob(self, nums: list[int]) -> int:
        assert nums

        a = b = 0

        for num in nums:
            a, b = b, max(num + a, b)

        return max(a, b)
