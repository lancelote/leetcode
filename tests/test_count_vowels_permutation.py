import pytest

from src.count_vowels_permutation import Solution


@pytest.mark.parametrize(
    "n,expected",
    (
        (1, 5),
        (2, 10),
        (5, 68),
    ),
)
def test_solution(n, expected):
    assert Solution().countVowelPermutation(n) == expected
