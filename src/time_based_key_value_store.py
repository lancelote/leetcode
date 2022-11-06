from bisect import bisect_right
from collections import defaultdict


class TimeMap:
    def __init__(self) -> None:
        self.data: dict[str, list[tuple[int, str]]] = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        i = bisect_right(self.data[key], timestamp, key=lambda x: x[0])
        if i > 0:
            return self.data[key][i - 1][1]
        return ""
