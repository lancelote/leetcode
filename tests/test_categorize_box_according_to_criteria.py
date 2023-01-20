import pytest

from src.categorize_box_according_to_criteria import Solution


@pytest.mark.parametrize(
    "params,expected",
    [
        ((1000, 35, 700, 300), "Heavy"),
        ((200, 50, 800, 50), "Neither"),
        ((2909, 3968, 3272, 727), "Both"),
        ((1000, 1000, 1000, 1000), "Both"),
        ((1, 1, 1, 100), "Heavy"),
        ((100000, 100000, 100000, 100), "Both"),
    ],
)
def test_solution(params, expected):
    assert Solution().categorizeBox(*params) == expected
