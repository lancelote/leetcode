class Solution:
    def alternateDigitSum(self, n: int) -> int:
        total = 0
        sign = +1

        for x in str(n):
            total += sign * int(x)
            sign *= -1

        return total
