from typing import TypeAlias

Cache: TypeAlias = dict[tuple[int, int], int]


def dp(n: int, k: int, target: int, cache: Cache) -> int:
    if n == 0:
        return 0 if target != 0 else 1

    if (n, target) in cache:
        return cache[(n, target)]

    result = 0
    for new_target in range(max(0, target - k), target):
        result += dp(n - 1, k, new_target, cache)
    cache[(n, target)] = result

    return result


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        return dp(n, k, target, cache={}) % (10**9 + 7)
