import pytest

from src.count_k_subsequences_of_a_string_with_maximum_beauty import Solution


@pytest.mark.parametrize(
    "s,k,expected",
    (
        ("bcca", 2, 4),
        ("abbcd", 4, 2),
        ("dd", 2, 0),
        ("fkp", 2, 3),
        ("ggsgo", 3, 3),
    ),
)
def test_solution(s, k, expected):
    assert Solution().countKSubsequencesWithMaxBeauty(s, k) == expected
