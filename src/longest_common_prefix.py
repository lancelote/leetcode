class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix_idx = 0

        for i in range(len(strs[0])):
            try:
                letter = strs[0][i]

                for word in strs:
                    if word[i] != letter:
                        return strs[0][:prefix_idx]

            except IndexError:
                break

            prefix_idx += 1

        return strs[0][:prefix_idx]
