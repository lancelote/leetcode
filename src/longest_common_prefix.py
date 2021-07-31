class Solution:
    def longestCommonPrefix(self, strings: list[str]) -> str:
        prefix = ""

        try:
            for i, char in enumerate(strings[0]):
                for string in strings:
                    if string[i] != char:
                        return prefix
                prefix += char
        except IndexError:
            ...

        return prefix
