import pytest

from src.zigzag_conversion import Solution


@pytest.mark.parametrize(
    "s,num_rows,expected",
    (
        ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
        ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
        ("A", 1, "A"),
        ("A", 2, "A"),
        ("AB", 1, "AB"),
    ),
)
def test_solution(s, num_rows, expected):
    assert Solution().convert(s, num_rows) == expected
