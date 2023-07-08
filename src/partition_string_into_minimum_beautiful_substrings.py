import sys


def is_power_of_5(num: int) -> bool:
    while num % 5 == 0:
        num //= 5
    return num == 1


class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        if s[0] == "0":
            return -1

        min_split = sys.maxsize

        def dfs(start: int, count: int) -> None:
            nonlocal min_split

            if start >= len(s):
                min_split = min(min_split, count)
                return

            num = []

            for i in range(start, len(s)):
                num.append(str(s[i]))

                if s[i] == "0":
                    continue
                elif i < len(s) - 1 and s[i + 1] == "0":
                    continue
                elif is_power_of_5(int("".join(num), base=2)):
                    dfs(i + 1, count + 1)

        dfs(0, 0)
        return min_split if min_split != sys.maxsize else -1
