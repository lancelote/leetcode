import math


class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            parts: list[str] = []
            for i in range(math.ceil(len(s) / k)):
                part = s[k * i : k * (i + 1)]
                parts.append(str(sum(int(x) for x in part)))
            s = "".join(parts)

        return s
