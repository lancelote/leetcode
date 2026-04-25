class Solution:
    def findTheDistanceValue(
        self, arr1: list[int], arr2: list[int], d: int
    ) -> int:
        arr2.sort()

        count = 0
        for x in arr1:
            left, right = 0, len(arr2) - 1
            while left <= right:
                middle = left + (right - left) // 2

                if abs(x - arr2[middle]) <= d:
                    count += 1
                    break

                if x < arr2[middle]:
                    right = middle - 1
                else:
                    left = middle + 1

        return len(arr1) - count
