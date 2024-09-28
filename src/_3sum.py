class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        sorted_nums = sorted(nums)

        result: list[list[int]] = []

        for i in range(n - 2):
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue  # skip duplicate

            x = sorted_nums[i]
            left, right = i + 1, n - 1

            while left < right:
                y = sorted_nums[left]
                z = sorted_nums[right]

                three_sum = x + y + z

                if three_sum == 0:
                    result.append([x, y, z])

                    left += 1
                    while (
                        left < right
                        and sorted_nums[left] == sorted_nums[left - 1]
                    ):
                        left += 1

                elif three_sum < 0:
                    left += 1
                else:
                    right -= 1

        return result
