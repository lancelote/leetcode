class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)
