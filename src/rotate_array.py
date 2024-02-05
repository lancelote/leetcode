def reverse(start: int, end: int, array: list[int]) -> None:
    n = end - start

    for i in range(n // 2):
        left = start + i
        right = end - i - 1

        array[left], array[right] = array[right], array[left]


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k = k % n

        reverse(0, n - k, nums)
        reverse(n - k, n, nums)
        reverse(0, n, nums)
