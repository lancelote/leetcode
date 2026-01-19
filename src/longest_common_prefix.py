class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        assert len(strs) >= 1

        prefix: list[str] = []

        for i in range(len(strs[0])):
            ch = strs[0][i]

            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != ch:
                    return "".join(prefix)

            prefix.append(ch)

        return "".join(prefix)
