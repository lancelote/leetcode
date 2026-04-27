import math

LIMIT = 2**31 // 10


class Solution:
    def reverse(self, x: int) -> int:
        result = 0

        while x != 0:
            digit = int(math.fmod(x, 10))

            if abs(result) > LIMIT:
                return 0

            if abs(result) == LIMIT and ((digit >= 8 and x > 0) or digit == -9):
                return 0

            result = result * 10 + digit
            x = math.trunc(x / 10)

        return result
