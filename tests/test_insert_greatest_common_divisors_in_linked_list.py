import pytest

from src.insert_greatest_common_divisors_in_linked_list import Solution
from src.utils.linked_list import to_linked_list
from src.utils.linked_list import to_list


@pytest.mark.parametrize(
    "in_list,out_list",
    (
        ([18, 6, 10, 3], [18, 6, 6, 2, 10, 1, 3]),
        ([7], [7]),
    ),
)
def test_solution(in_list, out_list):
    head = to_linked_list(in_list)
    result = Solution().insertGreatestCommonDivisors(head)
    assert to_list(result) == out_list
