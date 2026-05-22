class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def find_left() -> int:
            result = -1
            li, ri = 0, len(nums) - 1

            while li <= ri:
                m = li + (ri - li) // 2

                if nums[m] == target:
                    result = m
                    ri = m - 1
                elif nums[m] < target:
                    li = m + 1
                else:
                    ri = m - 1

            return result

        def find_right() -> int:
            result = -1
            li, ri = 0, len(nums) - 1

            while li <= ri:
                m = li + (ri - li) // 2

                if nums[m] == target:
                    result = m
                    li = m + 1
                elif nums[m] < target:
                    li = m + 1
                else:
                    ri = m - 1

            return result

        left = find_left()
        if left == -1:
            return [-1, -1]

        return [left, find_right()]
