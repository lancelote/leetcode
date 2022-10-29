class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 2147483647

        while b:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask

        return a if a <= mask // 2 else ~(a ^ mask)
