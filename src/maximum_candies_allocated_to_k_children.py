class Solution:
    def maximumCandies(self, candies: list[int], k: int) -> int:
        def can_allocate(n: int) -> bool:
            max_children = 0

            for pile in candies:
                max_children += pile // n

            return max_children >= k

        left, right = 0, max(candies)

        while left < right:
            middle = (left + right + 1) // 2

            if can_allocate(middle):
                left = middle
            else:
                right = middle - 1

        return left
