class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        n = len(arr)
        zeros = arr.count(0)

        for i in range(n - 1, -1, -1):
            if zeros == 0:
                break
            if i + zeros < n:
                arr[i + zeros] = arr[i]
            if arr[i] == 0:
                zeros -= 1
                if i + zeros < n:
                    arr[i + zeros] = 0
