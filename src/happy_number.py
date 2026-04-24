class Solution:
    def get_next(self, n: int) -> int:
        total = 0

        while n != 0:
            x = n % 10
            total += x * x
            n //= 10

        return total

    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.get_next(n)

        while fast != 1 and fast != slow:
            slow = self.get_next(slow)
            fast = self.get_next(self.get_next(fast))

        return fast == 1
