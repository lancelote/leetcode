from collections import defaultdict


class Solution:
    def countPairs(self, coordinates: list[list[int]], k: int) -> int:
        result = 0
        counts: dict[tuple[int, int], int] = defaultdict(int)

        for x, y in coordinates:
            for dk in range(k + 1):
                compliment = (x ^ dk, y ^ (k - dk))
                result += counts[compliment]
            counts[(x, y)] += 1

        return result
