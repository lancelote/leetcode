import pytest

from src.longest_common_prefix import Solution


@pytest.mark.parametrize(
    "strings,expected_prefix",
    [
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], ""),
        (["a"], "a"),
        (["ab", "a"], "a"),
    ],
)
def test_solution(strings, expected_prefix):
    assert Solution().longestCommonPrefix(strings) == expected_prefix
