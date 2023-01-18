import functools
import operator

POWERS_OF_4_XOR = functools.reduce(operator.xor, (4**x for x in range(16)))


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        is_power_of_two = n & (n - 1) == 0
        return n > 0 and is_power_of_two and (POWERS_OF_4_XOR & n == n)
