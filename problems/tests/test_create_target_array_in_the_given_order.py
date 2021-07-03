import pytest
from src.create_target_array_in_the_given_order import Solution


@pytest.mark.parametrize(
    "nums,index,output_array",
    [
        ([0, 1, 2, 3, 4], [0, 1, 2, 2, 1], [0, 4, 1, 3, 2]),
        ([1, 2, 3, 4, 0], [0, 1, 2, 3, 0], [0, 1, 2, 3, 4]),
        ([4, 2, 4, 3, 2], [0, 0, 1, 3, 1], [2, 2, 4, 4, 3]),
    ],
)
def test_solution(nums, index, output_array):
    assert Solution().createTargetArray(nums, index) == output_array
