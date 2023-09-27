import pytest

from src.decoded_string_at_index import Solution


@pytest.mark.parametrize(
    "s,k,expected",
    (
        ("leet2code3", 10, "o"),
        ("ha22", 5, "h"),
        ("a2345678999999999999999", 1, "a"),
    ),
)
def test_solution(s, k, expected):
    assert Solution().decodeAtIndex(s, k) == expected
