import pytest

from src.interleaving_string import Solution


@pytest.mark.parametrize(
    "s1,s2,s3,expected",
    (
        # ("aabcc"aabcc, "dbbca", "aadbbcbcac", True),
        ("aabcc", "dbbca", "aadbbbaccc", False),
        ("", "", "", True),
        ("", "", "a", False),
        ("a", "", "a", True),
        ("a", "b", "ab", True),
    ),
)
def test_solution(s1, s2, s3, expected):
    assert Solution().isInterleave(s1, s2, s3) is expected
