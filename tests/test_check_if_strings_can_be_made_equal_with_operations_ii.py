import pytest

from src.check_if_strings_can_be_made_equal_with_operations_ii import Solution


@pytest.mark.parametrize(
    "s1,s2,expected",
    (
        ("abcdba", "cabdab", True),
        ("abe", "bea", False),
    ),
)
def test_solution(s1, s2, expected):
    assert Solution().checkStrings(s1, s2) is expected
