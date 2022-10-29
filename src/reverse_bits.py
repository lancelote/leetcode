def clear_bit(i: int, n: int) -> int:
    return n & ~(1 << i)


def set_bit(i: int, n: int) -> int:
    return n | 1 << i


class Solution:
    def reverseBits(self, n: int) -> int:
        for i in range(16):
            lsbi = i
            msbi = 31 - i

            lsb = n & 1 << lsbi
            msb = n & 1 << msbi

            if lsb:
                n = set_bit(msbi, n)
            else:
                n = clear_bit(msbi, n)

            if msb:
                n = set_bit(lsbi, n)
            else:
                n = clear_bit(lsbi, n)

        return n
