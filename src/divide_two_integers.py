MAX_INT = 2147483647
MIN_INT = -2147483648


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        negative_nums = 2

        if dividend > 0:
            negative_nums -= 1
            dividend = -dividend

        if divisor > 0:
            negative_nums -= 1
            divisor = -divisor

        quotient = 0

        while dividend - divisor <= 0:
            quotient += 1
            dividend -= divisor

        return quotient if negative_nums != 1 else -quotient
