class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        cache: dict[int, int] = {}

        for i, num in enumerate(nums):
            if num in cache and i - cache[num] <= k:
                return True
            cache[num] = i

        return False
