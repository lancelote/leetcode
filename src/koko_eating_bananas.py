import math


class Solution:
    def will_take(self, k: int, piles: list[int]) -> int:
        return sum(int(math.ceil(pile / k)) for pile in piles)

    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left = 1
        right = max(piles)
        min_k = right

        while left <= right:
            k = left + (right - left) // 2
            eating_h = self.will_take(k, piles)

            if eating_h > h:
                left = k + 1
            else:
                right = k - 1
                min_k = min(min_k, k)

        return min_k
