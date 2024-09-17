import pytest

from src.summary_ranges import Solution


@pytest.mark.parametrize(
    "expected,nums",
    (
        (["0->2", "4->5", "7"], [0, 1, 2, 4, 5, 7]),
        (["0", "2->4", "6", "8->9"], [0, 2, 3, 4, 6, 8, 9]),
    ),
)
def test_solution(expected, nums):
    assert expected == Solution().summaryRanges(nums)
