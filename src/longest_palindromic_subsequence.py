def lcs(w1: str, w2: str) -> int:
    n1 = len(w1)
    n2 = len(w2)

    dp = [0] * (n2 + 1)

    for i1 in range(n1 - 1, -1, -1):
        new_dp = [0] * (n2 + 1)

        for i2 in range(n2 - 1, -1, -1):
            if w1[i1] == w2[i2]:
                new_dp[i2] = 1 + dp[i2 + 1]
            else:
                new_dp[i2] = max(new_dp[i2 + 1], dp[i2])

        dp = new_dp

    return dp[0]


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        assert s

        return lcs(s, s[::-1])
