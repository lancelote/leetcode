import pytest

from src.find_unique_binary_string import Solution


@pytest.mark.parametrize(
    "nums,expected",
    (
        (
            ["01", "10"],
            "00",
        ),
        (
            ["00", "01"],
            "10",
        ),
        (
            ["111", "011", "001"],
            "000",
        ),
        (
            ["11111", "01001", "00010", "10100", "11101"],
            "00000",
        ),
        (
            ["0"],
            "1",
        ),
    ),
)
def test_solution(nums, expected):
    assert Solution().findDifferentBinaryString(nums) == expected
