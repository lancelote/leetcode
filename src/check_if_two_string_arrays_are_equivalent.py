from itertools import zip_longest


class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        gen1 = (letter for part in word1 for letter in part)
        gen2 = (letter for part in word2 for letter in part)

        for x1, x2 in zip_longest(gen1, gen2, fillvalue=None):
            if x1 != x2:
                return False

        return True
