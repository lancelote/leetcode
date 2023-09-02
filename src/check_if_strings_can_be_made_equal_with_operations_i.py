from collections import Counter


class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        even_1 = Counter(s1[i] for i in range(0, len(s1), 2))
        odd_1 = Counter(s1[i] for i in range(1, len(s1), 2))
        even_2 = Counter(s2[i] for i in range(0, len(s2), 2))
        odd_2 = Counter(s2[i] for i in range(1, len(s2), 2))

        return even_1 == even_2 and odd_1 == odd_2
