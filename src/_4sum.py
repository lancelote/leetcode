class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        result: list[list[int]] = []

        sorted_nums = sorted(nums)
        n = len(sorted_nums)

        for i in range(n):
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue

            for j in range(i + 1, n):
                if j > i + 1 and sorted_nums[j] == sorted_nums[j - 1]:
                    continue

                left = j + 1
                right = n - 1

                while left < right:
                    a = sorted_nums[i]
                    b = sorted_nums[j]
                    c = sorted_nums[left]
                    d = sorted_nums[right]

                    if a + b + c + d == target:
                        result.append([a, b, c, d])
                        left += 1

                        while (
                            left < right
                            and sorted_nums[left] == sorted_nums[left - 1]
                        ):
                            left += 1

                        right -= 1
                    elif a + b + c + d < target:
                        left += 1
                    else:
                        right -= 1

        return result
