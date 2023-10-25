class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        total = 2 ** (n - 1)
        current = 0

        while k > 2:
            half = total // 2

            if k > half:
                k -= half
                current = 0 if current else 1
            else:
                current = 1 if current else 0

            total = half

        if current:
            return 1 if k == 1 else 0
        else:
            return 1 if k == 2 else 0
