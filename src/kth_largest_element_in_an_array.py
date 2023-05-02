class Solution:
    def quick_select(
        self, array: list[int], start: int, end: int, k: int
    ) -> int:
        n = len(array)

        if end - start < 1:
            return array[start]

        pivot = array[end]
        slow = start

        for i in range(start, end):
            if array[i] < pivot:
                tmp = array[slow]
                array[slow] = array[i]
                array[i] = tmp
                slow += 1

        array[end] = array[slow]
        array[slow] = pivot

        if n - slow == k:
            return pivot
        elif n - slow > k:
            return self.quick_select(array, slow + 1, end, k)
        else:
            return self.quick_select(array, start, slow - 1, k)

    def findKthLargest(self, nums: list[int], k: int) -> int:
        return self.quick_select(nums, 0, len(nums) - 1, k)
