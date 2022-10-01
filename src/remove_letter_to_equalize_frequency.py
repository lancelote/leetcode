from collections import Counter


class Solution:
    def equalFrequency(self, word: str) -> bool:
        for i in range(len(word)):
            counter = Counter(x for j, x in enumerate(word) if i != j)
            if len(set(counter.values())) == 1:
                return True
        return False
