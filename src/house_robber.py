class Solution:
    def rob(self, nums: list[int]) -> int:
        rob1 = 0
        rob2 = 0

        for n in nums:
            # [rob1, rob2, n, n+1, ...]
            tmp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = tmp

        return rob2
