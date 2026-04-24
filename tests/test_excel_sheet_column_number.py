import pytest

from src.excel_sheet_column_number import Solution


@pytest.mark.parametrize(
    "columnTitle,expected",
    (
        ("A", 1),
        ("AB", 28),
        ("ZY", 701),
    ),
)
def test_solution(columnTitle, expected):
    assert Solution().titleToNumber(columnTitle) == expected
