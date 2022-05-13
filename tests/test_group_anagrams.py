import pytest

from src.group_anagrams import Solution


@pytest.mark.parametrize(
    "strs,expected_list",
    [
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
        ),
        ([""], [[""]]),
        (["a"], [["a"]]),
    ],
)
def test_solution(strs, expected_list):
    result_list = list(Solution().groupAnagrams(strs))
    result_set = set(frozenset(x) for x in result_list)
    expected_set = set(frozenset(x) for x in expected_list)

    assert len(result_list) == len(expected_list)
    assert result_set == expected_set
