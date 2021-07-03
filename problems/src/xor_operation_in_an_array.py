class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        result = 0
        for i in range(start, n * 2 + start, 2):
            print(i)
            result ^= i
        return result
