from collections import defaultdict


class Solution:
    def countPoints(self, rings: str) -> int:
        rods: dict[int, set[str]] = defaultdict(set)
        for i in range(int(len(rings) / 2)):
            color = rings[i * 2]
            rod = int(rings[i * 2 + 1])
            rods[rod].add(color)
        return sum(1 for v in rods.values() if len(v) == 3)
