class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)

        dp = [0] * (n2 + 1)

        for i1 in range(n1 - 1, -1, -1):
            new_dp = [0] * (n2 + 1)

            for i2 in range(n2 - 1, -1, -1):
                if text1[i1] == text2[i2]:
                    new_dp[i2] = 1 + dp[i2 + 1]
                else:
                    new_dp[i2] = max(dp[i2], new_dp[i2 + 1])

            dp = new_dp

        return dp[0]
