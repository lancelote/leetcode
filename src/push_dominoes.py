import typing
from collections import deque


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        result = list(dominoes)
        queue: typing.Deque[tuple[int, str]] = deque()

        for i, x in enumerate(dominoes):
            if x != ".":
                queue.append((i, x))

        while queue:
            i, x = queue.popleft()

            if x == "L":
                if i > 0 and result[i - 1] == ".":
                    result[i - 1] = "L"
                    queue.append((i - 1, "L"))
            elif x == "R":
                if i + 1 < n and result[i + 1] == ".":
                    if i + 2 < n and result[i + 2] == "L":
                        queue.popleft()
                    else:
                        result[i + 1] = "R"
                        queue.append((i + 1, "R"))
            else:
                raise ValueError(f"unexpected domino: {x}")

        return "".join(result)
