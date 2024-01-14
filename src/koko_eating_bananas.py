import math


class Solution:
    def will_take(self, mid: int, piles: list[int]) -> int:
        return sum(int(math.ceil(pile / mid)) for pile in piles)

    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left = 1
        right = max(piles)
        min_mid = right

        while left <= right:
            mid = (left + right) // 2
            t = self.will_take(mid, piles)

            if t > h:
                left = mid + 1
            else:
                right = mid - 1
                min_mid = min(min_mid, mid)

        return min_mid
