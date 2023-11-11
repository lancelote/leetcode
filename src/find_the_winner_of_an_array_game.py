from collections import deque


class Solution:
    def getWinner(self, arr: list[int], k: int) -> int:
        k = min(len(arr), k)

        a, b = arr[0], arr[1]
        d: deque[int] = deque()

        for i in range(2, len(arr)):
            d.append(arr[i])

        win_count = 0

        while win_count < k:
            if a > b:
                d.append(b)
                b = d.popleft()
                win_count += 1
            else:
                d.append(a)
                a = b
                b = d.popleft()
                win_count = 1

        return a
