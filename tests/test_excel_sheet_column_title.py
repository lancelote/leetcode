import pytest

from src.excel_sheet_column_title import Solution


@pytest.mark.parametrize(
    "column_number,expected",
    (
        (1, "A"),
        (28, "AB"),
        (701, "ZY"),
    ),
)
def test_solution(column_number, expected):
    assert Solution().convertToTitle(column_number) == expected
