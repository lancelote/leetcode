class Solution:
    def hIndex(self, citations: list[int]) -> int:
        n = len(citations)

        counts = [0] * (n + 1)

        for x in citations:
            counts[min(n, x)] += 1

        h = 0
        rest = n

        for x, count in enumerate(counts):
            h = max(h, min(x, rest))
            rest -= count

        return h
