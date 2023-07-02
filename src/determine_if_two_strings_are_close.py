from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        if set(word1) != set(word2):
            return False

        c1 = Counter(word1)
        c2 = Counter(word2)

        for (_, x1), (_, x2) in zip(c1.most_common(), c2.most_common()):
            if x1 != x2:
                return False

        return True
