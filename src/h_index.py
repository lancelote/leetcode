class Solution:
    def hIndex(self, citations: list[int]) -> int:
        sorted_citations = sorted(citations, reverse=True)
        h = 0

        for i, x in enumerate(sorted_citations, start=1):
            h = max(h, min(i, x))

        return h
