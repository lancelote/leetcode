import pytest

from src.minimum_genetic_mutation import Solution


@pytest.mark.parametrize(
    "start,end,bank,expected",
    [
        ("AACCGGTT", "AACCGGTA", ["AACCGGTA"], 1),
        ("AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"], 2),
        ("AAAAACCC", "AACCCCCC", ["AAAACCCC", "AAACCCCC", "AACCCCCC"], 3),
    ],
)
def test_solution(start, end, bank, expected):
    assert Solution().minMutation(start, end, bank) == expected
