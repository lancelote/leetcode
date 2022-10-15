import pytest

from src.string_compression_ii import Solution


@pytest.mark.parametrize(
    "s,k,expected",
    [
        ("aaabcccd", 2, 4),
        ("aabbaa", 2, 2),
        ("aaaaaaaaaaa", 0, 3),
    ],
)
def test_solution(s, k, expected):
    assert Solution().getLengthOfOptimalCompression(s, k) == expected
