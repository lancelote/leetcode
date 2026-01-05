class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        soldiers = [sum(row) for row in mat]
        n = len(soldiers)
        stronger: list[int] = [0] * n

        for i in range(n):
            for j in range(i + 1, n):
                if soldiers[i] > soldiers[j]:
                    stronger[i] += 1
                elif soldiers[i] == soldiers[j] and i > j:
                    stronger[i] += 1
                else:
                    stronger[j] += 1

        stronger_pairs = [(x, i) for i, x in enumerate(stronger)]

        return [i for _, i in sorted(stronger_pairs)][:k]
