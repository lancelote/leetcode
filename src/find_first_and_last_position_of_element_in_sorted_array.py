class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def get_middle_idx() -> int:
            left = 0
            right = len(nums) - 1

            while left <= right:
                middle = left + (right - left) // 2

                if nums[middle] == target:
                    return middle
                elif nums[middle] > target:
                    right = middle - 1
                else:
                    left = middle + 1

            return -1

        def get_left_idx(right: int) -> int:
            result = right
            left = 0

            while left <= right:
                middle = left + (right - left) // 2

                if nums[middle] == target:
                    result = middle
                    right = middle - 1
                elif nums[middle] > target:
                    right = middle - 1
                else:
                    left = middle + 1

            return result

        def get_right_idx(left: int) -> int:
            result = left
            right = len(nums) - 1

            while left <= right:
                middle = left + (right - left) // 2

                if nums[middle] == target:
                    result = middle
                    left = middle + 1
                elif nums[middle] > target:
                    right = middle - 1
                else:
                    left = middle + 1

            return result

        middle_idx = get_middle_idx()

        if middle_idx == -1:
            return [-1, -1]

        left_idx = get_left_idx(right=middle_idx)
        right_idx = get_right_idx(left=middle_idx)

        return [left_idx, right_idx]
