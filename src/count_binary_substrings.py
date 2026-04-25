class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        result = 0

        zeros = 0
        ones = 0

        if s[0] == "0":
            zeros += 1
        else:
            ones += 1

        for i in range(1, len(s)):
            if zeros and ones and s[i] != s[i - 1]:
                if s[i] == "0":
                    zeros = 1
                else:
                    ones = 1
            elif s[i] == "0":
                zeros += 1
            else:
                ones += 1

            if s[i] == "0" and zeros <= ones:
                result += 1

            if s[i] == "1" and ones <= zeros:
                result += 1

        return result
