class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [0] * (len(t) + 1)
        dp[-1] = 1

        for j in range(len(s) - 1, -1, -1):
            new_dp = [0] * (len(t) + 1)
            new_dp[-1] = 1

            for i in range(len(t) - 1, -1, -1):
                new_dp[i] = dp[i]

                if s[j] == t[i]:
                    new_dp[i] += dp[i + 1]

            dp = new_dp

        return dp[0]
