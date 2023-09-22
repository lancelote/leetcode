class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)

        i1 = i2 = 0

        while i1 < n and i2 < m:
            if s[i1] == t[i2]:
                i1 += 1
                i2 += 1
            else:
                i2 += 1

        return i1 == n
