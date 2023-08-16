class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)

        dp = [x for x in range(n2, -1, -1)]

        for i1 in range(n1 - 1, -1, -1):
            new_dp = [0] * (n2 + 1)
            new_dp[-1] = n1 - i1

            for i2 in range(n2 - 1, -1, -1):
                if word1[i1] == word2[i2]:
                    new_dp[i2] = min(
                        1 + dp[i2],
                        dp[i2 + 1],
                        1 + new_dp[i2 + 1],
                    )
                else:
                    new_dp[i2] = min(
                        1 + dp[i2],
                        1 + dp[i2 + 1],
                        1 + new_dp[i2 + 1],
                    )

            dp = new_dp
        return dp[0]
