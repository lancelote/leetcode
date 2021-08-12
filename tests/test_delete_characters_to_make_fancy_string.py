import pytest

from src.delete_characters_to_make_fancy_string import Solution


@pytest.mark.parametrize(
    "input_string,filtered_string",
    [
        ("leeetcode", "leetcode"),
        ("aaabaaaa", "aabaa"),
        ("aab", "aab"),
    ],
)
def test_solution(input_string, filtered_string):
    assert Solution().makeFancyString(input_string) == filtered_string
