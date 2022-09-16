class Solution:
    def maximumScore(self, nums: list[int], multipliers: list[int]) -> int:
        m = len(multipliers)
        n = len(nums)

        dp = [[0] * (m + 1) for _ in range(m + 1)]

        for op in range(m - 1, -1, -1):
            for left in range(op, -1, -1):
                right = n - 1 - (op - left)

                first = multipliers[op] * nums[left] + dp[op + 1][left + 1]
                last = multipliers[op] * nums[right] + dp[op + 1][left]

                dp[op][left] = max(first, last)

        return dp[0][0]
