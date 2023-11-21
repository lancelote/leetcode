from collections import defaultdict

MOD = 10**9 + 7


class Solution:
    def countNicePairs(self, nums: list[int]) -> int:
        compliment: dict[int, int] = defaultdict(int)

        for x in nums:
            compliment[x - int(str(x)[::-1])] += 1

        return sum(x * (x - 1) // 2 for x in compliment.values()) % MOD
