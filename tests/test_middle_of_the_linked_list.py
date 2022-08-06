import pytest

from src.middle_of_the_linked_list import Solution
from src.utils.linked_list import to_linked_list
from src.utils.linked_list import to_list


@pytest.mark.parametrize(
    "input_array,expected_array",
    [
        ([1, 2, 3, 4, 5], [3, 4, 5]),
        ([1, 2, 3, 4, 5, 6], [4, 5, 6]),
    ],
)
def test_solution(input_array, expected_array):
    head = to_linked_list(input_array)
    middle_node = Solution().middleNode(head)
    result_array = to_list(middle_node)
    assert result_array == expected_array
