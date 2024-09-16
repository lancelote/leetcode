class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lps = [0] * len(needle)

        prev_lps = 0
        i = 1

        while i < len(needle):
            if needle[i] == needle[prev_lps]:
                lps[i] = prev_lps + 1
                prev_lps += 1
                i += 1
            elif prev_lps == 0:
                lps[i] = 0
                i += 1
            else:
                prev_lps = lps[prev_lps - 1]

        i = 0  # ptr for haystack
        j = 0  # ptr for needle

        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j - 1]
            if j == len(needle):
                return i - len(needle)

        return -1
