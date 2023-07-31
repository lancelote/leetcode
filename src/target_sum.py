class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        cache = {0: 1}

        for num in nums:
            new_cache: dict[int, int] = {}

            for k, v in cache.items():
                new_cache[k + num] = new_cache.get(k + num, 0) + v
                new_cache[k - num] = new_cache.get(k - num, 0) + v

            cache = new_cache

        return cache.get(target, 0)
