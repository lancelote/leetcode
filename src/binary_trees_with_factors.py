from collections import defaultdict


MOD = 10**9 + 7


class Solution:
    def numFactoredBinaryTrees(self, arr: list[int]) -> int:
        cache: dict[int, int] = defaultdict(int)
        sorted_arr = sorted(arr)

        for i, x in enumerate(sorted_arr):
            options = 1

            for j in range(i):
                if x % sorted_arr[j] == 0:
                    a = x // sorted_arr[j]
                    b = x // a

                    options += cache[a] * cache[b]

            cache[x] = options

        return sum(cache.values()) % MOD
