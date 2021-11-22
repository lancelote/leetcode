import pytest

from src.decrypt_string_from_alphabet_to_integer_mapping import Solution


@pytest.mark.parametrize(
    "s,expected",
    [
        ("10#11#12", "jkab"),
        ("1326#", "acz"),
        ("25#", "y"),
        (
            "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#",
            "abcdefghijklmnopqrstuvwxyz",
        ),
    ],
)
def test_solution(s, expected):
    assert Solution().freqAlphabets(s) == expected
