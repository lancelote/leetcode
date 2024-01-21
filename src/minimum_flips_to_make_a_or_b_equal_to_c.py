class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0

        while a or b != c:
            bit_a = a & 1
            bit_b = b & 1
            bit_c = c & 1

            if (bit_a or bit_b) != bit_c:
                if bit_a and bit_b and not bit_c:
                    flips += 2
                else:
                    flips += 1

            a >>= 1
            b >>= 1
            c >>= 1

        return flips
