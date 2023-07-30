class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2
        seen = {0}

        for i in range(len(nums) - 1, -1, -1):
            for x in set(seen):
                new_sum = nums[i] + x

                if new_sum == target:
                    return True

                seen.add(new_sum)

        return False
