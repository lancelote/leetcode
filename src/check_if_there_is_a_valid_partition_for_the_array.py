class Solution:
    def validPartition(self, nums: list[int]) -> bool:
        n = len(nums)
        cache: dict[int, bool] = {}

        def dfs(i: int) -> bool:
            if i >= n:
                return True
            if i in cache:
                return cache[i]

            two = i < n - 1 and nums[i] == nums[i + 1]
            three = i < n - 2 and nums[i] == nums[i + 1] == nums[i + 2]
            increase = (
                i < n - 2 and nums[i] + 2 == nums[i + 1] + 1 == nums[i + 2]
            )

            if two:
                cache[i + 2] = dfs(i + 2)
                if cache[i + 2]:
                    return True

            if three or increase:
                cache[i + 3] = dfs(i + 3)
                if cache[i + 3]:
                    return True

            return False

        return dfs(0)
