class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        bin_val = bin(n)[2:]
        n = len(bin_val)
        zeros = bin_val.count("0")
        return bin_val[0] == "1" and zeros == n - 1 and zeros % 2 == 0
