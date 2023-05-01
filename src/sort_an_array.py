class Solution:
    def quick_sort(self, array: list[int], start: int, end: int) -> None:
        if end - start < 1:
            return

        pivot = array[end]

        slow = start
        for i in range(start, end):
            if array[i] < pivot:
                tmp = array[i]
                array[i] = array[slow]
                array[slow] = tmp
                slow += 1

        array[end] = array[slow]
        array[slow] = pivot

        self.quick_sort(array, start, slow - 1)
        self.quick_sort(array, slow + 1, end)

    def sortArray(self, nums: list[int]) -> list[int]:
        self.quick_sort(nums, start=0, end=len(nums) - 1)
        return nums
