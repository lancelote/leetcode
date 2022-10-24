import pytest

import src.maximum_length_of_a_concatenated_string_with_unique_characters as s


@pytest.mark.parametrize(
    "arr,expected",
    [
        (["un", "iq", "ue"], 4),
        (["cha", "r", "act", "ers"], 6),
        (["abcdefghijklmnopqrstuvwxyz"], 26),
        (["aa", "bb"], 0),
    ],
)
def test_solution(arr, expected):
    assert s.Solution().maxLength(arr) == expected
