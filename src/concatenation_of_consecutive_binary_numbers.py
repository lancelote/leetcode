class Solution:
    def concatenatedBinary(self, n: int) -> int:
        result: list[str] = []

        for x in range(1, n + 1):
            bin_x = bin(x)[2:]
            result.append(bin_x)

        return int("".join(result), base=2) % (10**9 + 7)
