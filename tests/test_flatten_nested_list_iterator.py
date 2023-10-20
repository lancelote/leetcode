import pytest

from src.flatten_nested_list_iterator import NestedInteger
from src.flatten_nested_list_iterator import NestedIterator


@pytest.mark.parametrize(
    "in_list, expected",
    (
        ([[1, 1], 2, [1, 1]], [1, 1, 2, 1, 1]),
        ([1, [4, [6]]], [1, 4, 6]),
    ),
)
def test_solution(in_list, expected):
    actual: list[int] = []

    nested_list = NestedInteger.from_list(in_list)
    nested_iter = NestedIterator(nested_list)

    while nested_iter.hasNext():
        actual.append(nested_iter.next())

    assert actual == expected
