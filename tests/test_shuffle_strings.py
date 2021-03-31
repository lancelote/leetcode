import pytest

from src.shuffle_strings import Solution


@pytest.mark.parametrize(
    "text,indexes,expected_string",
    [
        ("codeleet", [4, 5, 6, 7, 0, 2, 1, 3], "leetcode"),
        ("abc", [0, 1, 2], "abc"),
        ("aiohn", [3, 1, 4, 2, 0], "nihao"),
        ("aaiougrt", [4, 0, 2, 6, 7, 3, 1, 5], "arigatou"),
        ("art", [1, 0, 2], "rat"),
    ],
)
def test_solution(text, indexes, expected_string):
    assert Solution().restoreString(text, indexes) == expected_string
