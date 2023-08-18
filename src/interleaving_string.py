class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)

        if n1 + n2 != n3:
            return False

        dp = [False] * (n2 + 1)
        dp[-1] = True

        for i2 in range(n2 - 1, -1, -1):
            dp[i2] = s3[n1 + i2] == s2[i2] and dp[i2 + 1]

        for i1 in range(n1 - 1, -1, -1):
            new_dp = [False] * (n2 + 1)
            new_dp[-1] = s3[n2 + i1] == s1[i1] and dp[-1]

            for i2 in range(n2 - 1, -1, -1):
                if s3[i1 + i2] == s1[i1]:
                    new_dp[i2] |= dp[i2]
                if s3[i1 + i2] == s2[i2]:
                    new_dp[i2] |= new_dp[i2 + 1]

            dp = new_dp

        return dp[0]
