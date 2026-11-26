class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen: dict[str, int] = {}
        discarded: set[str] = set()

        for i, x in enumerate(s):
            if x in seen:
                del seen[x]
                discarded.add(x)
            elif x in discarded:
                continue
            else:
                seen[x] = i

        for v in seen.values():
            return v

        return -1
