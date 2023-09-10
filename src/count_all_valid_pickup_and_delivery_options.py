class Solution:
    def countOrders(self, n: int) -> int:
        slots = n * 2
        result = 1

        while slots > 0:
            options = slots * (slots - 1) // 2
            result *= options
            slots -= 2

        return result % (10**9 + 7)
