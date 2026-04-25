class Solution:
    def fixedPoint(self, arr: list[int]) -> int:
        result = -1

        left, right = 0, len(arr) - 1
        while left <= right:
            middle = left + (right - left) // 2

            if middle == arr[middle]:
                result = middle
                right = middle - 1
            elif middle < arr[middle]:
                right = middle - 1
            else:
                left = middle + 1

        return result
