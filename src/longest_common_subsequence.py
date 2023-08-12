class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)

        dp = [0] * (m + 1)

        for i in range(n):
            new_dp = [0] * (m + 1)

            for j in range(m):
                if text1[i] == text2[j]:
                    new_dp[j + 1] = 1 + dp[j]
                else:
                    new_dp[j + 1] = max(dp[j + 1], new_dp[j])

            dp = new_dp

        return dp[-1]
