class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0

        for shift in range(32):
            result |= (n & 1 << shift != 0) << (31 - shift)

        return result
