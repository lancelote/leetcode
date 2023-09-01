class Solution:
    def countBits(self, n: int) -> list[int]:
        result = [0] * (n + 1)
        shift = 1

        for i in range(1, n + 1):
            if shift * 2 == i:
                shift = i

            result[i] = 1 + result[i - shift]

        return result
