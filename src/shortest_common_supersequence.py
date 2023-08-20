def lcs(str1: str, str2: str) -> str:
    n1 = len(str1)
    n2 = len(str2)

    dp = ["" for _ in range(n2 + 1)]

    for i1 in range(n1):
        new_dp = ["" for _ in range(n2 + 1)]

        for i2 in range(n2):
            if str1[i1] == str2[i2]:
                new_dp[i2 + 1] = dp[i2] + str2[i2]
            else:
                new_dp[i2 + 1] = max(dp[i2 + 1], new_dp[i2], key=len)

        dp = new_dp

    return dp[-1]


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n1 = len(str1)
        n2 = len(str2)

        result: list[str] = []
        i1 = i2 = 0

        for x in lcs(str1, str2):
            while str1[i1] != x:
                result.append(str1[i1])
                i1 += 1
            while str2[i2] != x:
                result.append(str2[i2])
                i2 += 1

            result.append(x)
            i1 += 1
            i2 += 1

        while i1 < n1:
            result.append(str1[i1])
            i1 += 1

        while i2 < n2:
            result.append(str2[i2])
            i2 += 1

        return "".join(result)
