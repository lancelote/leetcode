def get_smallest__value_idx(nums: list[int]) -> int:
    smallest = nums[0]
    smallest_idx = 0
    for i, num in enumerate(nums):
        if num < smallest:
            smallest = num
            smallest_idx = i
    return smallest_idx


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        assert nums

        smallest_value_idx = get_smallest__value_idx(nums)
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle_idx = (right - left) // 2 + left
            middle_value = nums[(middle_idx + smallest_value_idx) % len(nums)]

            if middle_value == target:
                return (middle_idx + smallest_value_idx) % len(nums)
            elif middle_value < target:
                left = middle_idx + 1
            else:
                right = middle_idx - 1

        return -1
