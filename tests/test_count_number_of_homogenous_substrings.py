import pytest

from src.count_number_of_homogenous_substrings import Solution


@pytest.mark.parametrize(
    "s,expected",
    (
        ("abbcccaa", 13),
        ("xy", 2),
        ("zzzzz", 15),
    ),
)
def test_solution(s, expected):
    assert Solution().countHomogenous(s) == expected
