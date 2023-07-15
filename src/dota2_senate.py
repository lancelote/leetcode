from collections import deque
from typing import Deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)

        r: Deque[int] = deque()
        d: Deque[int] = deque()

        for i, x in enumerate(senate):
            if x == "R":
                r.append(i)
            else:
                d.append(i)

        while r and d:
            if r[0] < d[0]:
                d.popleft()
                r.append(r.popleft() + n)
            else:
                d.append(d.popleft() + n)
                r.popleft()

        return "Radiant" if r else "Dire"
