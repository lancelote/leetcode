class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        for i, x in enumerate(strs[0]):
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != x:
                    return strs[0][:i]
        return strs[0]
