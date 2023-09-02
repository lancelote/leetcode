import pytest

from src.check_if_strings_can_be_made_equal_with_operations_i import Solution


@pytest.mark.parametrize(
    "s1,s2,expected",
    (
        ("abcd", "cdab", True),
        ("abcd", "dacb", False),
    ),
)
def test_solution(s1, s2, expected):
    assert Solution().canBeEqual(s1, s2) is expected
