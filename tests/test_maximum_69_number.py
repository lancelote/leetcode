import pytest

from src.maximum_69_number import Solution


@pytest.mark.parametrize(
    "num,expected",
    [
        (9669, 9969),
        (9996, 9999),
        (9999, 9999),
    ],
)
def test_solution(num, expected):
    assert Solution().maximum69Number(num) == expected
