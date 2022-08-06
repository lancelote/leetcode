import typing
from collections import defaultdict
from typing import TypeAlias

Item: TypeAlias = list[int]
Items: TypeAlias = list[list[int]]


class Solution:
    def mergeSimilarItems(self, items1: Items, items2: Items) -> Items:
        result_map: typing.DefaultDict[int, int] = defaultdict(int)

        for v, w in items1:
            result_map[v] = w
        for v, w in items2:
            result_map[v] += w

        return [list(x) for x in sorted(result_map.items())]
