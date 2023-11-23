import pytest

from src.arithmetic_subarrays import Solution


@pytest.mark.parametrize(
    "nums,lefts_ids,right_ids,expected",
    (
        ([4, 6, 5, 9, 3, 7], [0, 0, 2], [2, 3, 5], [True, False, True]),
        (
            [-12, -9, -3, -12, -6, 15, 20, -25, -20, -15, -10],
            [0, 1, 6, 4, 8, 7],
            [4, 4, 9, 7, 9, 10],
            [False, True, False, False, True, True],
        ),
    ),
)
def test_solution(nums, lefts_ids, right_ids, expected):
    assert (
        Solution().checkArithmeticSubarrays(nums, lefts_ids, right_ids)
        == expected
    )
