import pytest

from src.visit_array_positions_to_maximize_score import Solution


@pytest.mark.parametrize(
    "nums,x,expected",
    (
        ([2, 3, 6, 1, 9, 2], 5, 13),
        ([2, 4, 6, 8], 3, 20),
        ([2, 99], 50, 51),
        (
            [
                82,
                1,
                76,
                43,
                4,
                15,
                86,
                63,
                10,
                1,
                45,
                93,
                52,
                97,
                78,
                61,
                53,
                50,
                98,
                73,
                58,
                9,
                93,
                88,
                63,
                61,
                39,
                8,
                70,
                29,
                17,
                22,
                75,
                40,
                75,
                35,
                58,
                64,
                56,
                86,
                5,
            ],
            72,
            1354,
        ),
    ),
)
def test_solution(nums, x, expected):
    assert Solution().maxScore(nums, x) == expected
