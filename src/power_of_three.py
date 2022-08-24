from math import log

MAX_INT = 2**31 - 1
MAX_POWER_OF_3 = 3 ** int(log(MAX_INT, 3))


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and MAX_POWER_OF_3 % n == 0
