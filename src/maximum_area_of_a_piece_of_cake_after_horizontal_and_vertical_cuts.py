from collections.abc import Iterator
from itertools import chain


def pieces(limit: int, cuts: list[int]) -> Iterator[int]:
    current = 0

    for cut in chain(sorted(cuts), (limit,)):
        yield cut - current
        current = cut


class Solution:
    def maxArea(
        self,
        h: int,
        w: int,
        horizontalCuts: list[int],
        verticalCuts: list[int],
    ) -> int:
        longest_h = max(pieces(h, horizontalCuts))
        longest_v = max(pieces(w, verticalCuts))

        return (longest_h * longest_v) % (10**9 + 7)
