from collections.abc import Iterator
from itertools import zip_longest


def next_char(s: str) -> Iterator[str]:
    i = len(s) - 1
    shift = 0

    while i >= 0:
        if s[i] != "#" and not shift:
            yield s[i]
        elif s[i] != "#" and shift:
            shift -= 1
        else:
            shift += 1
        i -= 1


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        iter1 = next_char(s)
        iter2 = next_char(t)

        for a, b in zip_longest(iter1, iter2, fillvalue=""):
            if a != b:
                return False

        return True
