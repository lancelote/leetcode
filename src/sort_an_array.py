class Solution:
    def merge_sort(self, array: list[int], start: int, end: int) -> None:
        if end - start <= 1:
            return

        middle = (start + end) // 2

        self.merge_sort(array, start, middle)
        self.merge_sort(array, middle, end)

        self.merge(array, start, end)

    def merge(self, array: list[int], start: int, end: int) -> None:
        length = end - start
        middle = (start + end) // 2

        tmp = [0] * length

        left = 0
        right = 0

        while start + left < middle and middle + right < end:
            if array[start + left] < array[middle + right]:
                tmp[left + right] = array[start + left]
                left += 1
            else:
                tmp[left + right] = array[middle + right]
                right += 1

        while start + left < middle:
            tmp[left + right] = array[start + left]
            left += 1

        while middle + right < end:
            tmp[left + right] = array[middle + right]
            right += 1

        for i in range(start, end):
            array[i] = tmp[i - start]

    def sortArray(self, nums: list[int]) -> list[int]:
        self.merge_sort(nums, 0, len(nums))
        return nums
