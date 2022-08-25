import pytest

from src.ransom_note import Solution


@pytest.mark.parametrize(
    "ransom_note,magazine,expected",
    [
        ("a", "b", False),
        ("aa", "ab", False),
        ("aa", "aab", True),
    ],
)
def test_solution(ransom_note, magazine, expected):
    assert Solution().canConstruct(ransom_note, magazine) is expected
