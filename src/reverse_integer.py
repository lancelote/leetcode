class Solution:
    def reverse(self, x: int) -> int:
        result = int(str(abs(x))[::-1])

        if -(2**31) - 1 < result < 2**31:
            return -result if x < 0 else result

        return 0
