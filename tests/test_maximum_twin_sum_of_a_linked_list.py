import pytest

from src.maximum_twin_sum_of_a_linked_list import Solution
from src.utils.linked_list import to_linked_list


@pytest.mark.parametrize(
    "in_list,expected",
    (
        ([5, 4, 2, 1], 6),
        ([4, 2, 2, 3], 7),
        ([1, 100_000], 100_001),
    ),
)
def test_solution(in_list, expected):
    head = to_linked_list(in_list)
    assert Solution().pairSum(head) == expected
