class Solution:
    def reverseDegree(self, s: str) -> int:
        return sum(
            i * (26 - ord(x) + ord("a")) for i, x in enumerate(s, start=1)
        )
