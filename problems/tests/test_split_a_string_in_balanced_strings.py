import pytest
from src.split_a_string_in_balanced_strings import Solution


@pytest.mark.parametrize(
    "line,balanced_splits",
    [
        ("RLRRLLRLRL", 4),
        ("RLLLLRRRLR", 3),
        ("LLLLRRRR", 1),
        ("RLRRRLLRLL", 2),
    ],
)
def test_solution(line, balanced_splits):
    assert Solution().balancedStringSplit(line) == balanced_splits
