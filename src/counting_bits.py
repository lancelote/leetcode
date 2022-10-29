class Solution:
    def countBits(self, n: int) -> list[int]:
        result: list[int] = []

        for x in range(n + 1):
            count = 0

            while x:
                x = x & (x - 1)
                count += 1

            result.append(count)

        return result
