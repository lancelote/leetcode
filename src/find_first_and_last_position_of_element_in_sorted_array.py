import math


def find_any_index(nums: list[int], target: int) -> int:
    n = len(nums)
    left, right = 0, n

    while left < right:
        middle = (right - left) // 2 + left

        if nums[middle] == target:
            return middle
        elif nums[middle] > target:
            right = middle
        else:
            left = middle + 1

    return -1


def find_left_index(nums: list[int], any_index: int, target: int) -> int:
    assert any_index != -1

    left, right = 0, any_index

    while left < right:
        middle = (right - left) // 2 + left

        if nums[middle] == target:
            right = middle
        elif nums[middle] > target:
            raise ValueError
        else:
            left = middle + 1

    return right


def find_right_index(nums: list[int], any_index: int, target: int) -> int:
    assert any_index != -1

    n = len(nums)
    left, right = any_index, n - 1

    while left < right:
        middle = math.ceil((right - left) / 2) + left

        if nums[middle] == target:
            left = middle
        elif nums[middle] < target:
            raise ValueError
        else:
            right = middle - 1

    return left


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        any_index = find_any_index(nums, target)

        if any_index == -1:
            return [-1, -1]

        left_index = find_left_index(nums, any_index, target)
        right_index = find_right_index(nums, any_index, target)

        return [left_index, right_index]
