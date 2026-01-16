class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        if k == 0:
            return False

        n = len(nums)

        seen: set[int] = set()

        for i in range(min(k, n)):
            if nums[i] in seen:
                return True

            seen.add(nums[i])

        for i in range(k, len(nums)):
            if nums[i] in seen:
                return True

            seen.discard(nums[i - k])
            seen.add(nums[i])

        return False
