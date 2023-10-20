from __future__ import annotations

from collections.abc import Iterator
from typing import Any


class NestedInteger:
    @classmethod
    def from_list(cls, data: list[Any]) -> list[NestedInteger]:
        result: list[NestedInteger] = []

        for x in data:
            if isinstance(x, int):
                result.append(NestedInteger(x))
            else:
                result.append(NestedInteger(NestedInteger.from_list(x)))

        return result

    def __init__(self, data: int | list[NestedInteger]) -> None:
        self.data = data

    def isInteger(self) -> bool:
        return isinstance(self.data, int)

    def getInteger(self) -> int:
        assert isinstance(self.data, int)
        return self.data

    def getList(self) -> list[NestedInteger]:
        assert isinstance(self.data, list)
        return self.data


def get_items(nested_list: list[NestedInteger]) -> Iterator[int]:
    for x in nested_list:
        if x.isInteger():
            yield x.getInteger()
        else:
            yield from get_items(x.getList())


def flatten(nested_list: list[NestedInteger]) -> list[int]:
    return [x for x in get_items(nested_list)]


class NestedIterator:
    def __init__(self, nested_list: list[NestedInteger]):
        self.data = flatten(nested_list)
        self.i = 0

    def next(self) -> int:
        item = self.data[self.i]
        self.i += 1
        return item

    def hasNext(self) -> bool:
        return self.i < len(self.data)
