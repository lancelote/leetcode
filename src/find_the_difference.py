from collections import Counter
from collections import defaultdict


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count0: dict[str, int] = Counter(s)
        count1: dict[str, int] = defaultdict(int)

        for x in t:
            count1[x] += 1
            if count1[x] > count0[x]:
                return x

        raise ValueError
