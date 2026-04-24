class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n = len(columnTitle)
        total = 0
        mult = 1

        for i in range(n - 1, -1, -1):
            total += (ord(columnTitle[i]) - 64) * mult
            mult *= 26

        return total
