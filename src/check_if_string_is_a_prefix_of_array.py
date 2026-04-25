class Solution:
    def isPrefixString(self, s: str, words: list[str]) -> bool:
        i1, i2 = 0, 0

        while i1 < len(s):
            if i2 == len(words):
                return False

            for j in range(len(words[i2])):
                if i1 == len(s):
                    return False

                if s[i1] != words[i2][j]:
                    return False

                i1 += 1

            i2 += 1

        return True
