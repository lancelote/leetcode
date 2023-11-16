class Solution:
    def maximumElementAfterDecrementingAndRearranging(
        self, arr: list[int]
    ) -> int:
        arr = sorted(arr)

        last = 0

        for x in arr:
            if x > last + 1:
                last = last + 1
            else:
                last = x

        return last
