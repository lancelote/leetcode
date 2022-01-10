from collections import Counter
from itertools import chain


class Solution:
    def sortString(self, s: str) -> str:
        chars = sorted(set(s))
        counter = Counter(s)
        result = []

        while sum(counter.values()) != 0:
            for char in chain(chars, reversed(chars)):
                if char in counter:
                    result.append(char)
                    counter[char] -= 1
                if counter[char] == 0:
                    del counter[char]

        return "".join(result)
