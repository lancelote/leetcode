import pytest

from src.time_needed_to_rearrange_a_binary_string import Solution


@pytest.mark.parametrize(
    "s,expected_time",
    [
        ("0110101", 4),
        ("11100", 0),
        ("001011", 4),
        ("001000011", 7),
        ("1", 0),
        ("0", 0),
        ("10", 0),
        ("11", 0),
        ("0111", 3),
        ("1101", 1),
        ("1001111111110001011001110000000110101", 20),
        ("011001", 3),
        ("01101", 3),
    ],
)
def test_solution(s, expected_time):
    assert Solution().secondsToRemoveOccurrences(s) == expected_time
