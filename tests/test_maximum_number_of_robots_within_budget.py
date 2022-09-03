import pytest

from src.maximum_number_of_robots_within_budget import Solution


@pytest.mark.parametrize(
    "charge_times,running_costs,budget,expected",
    [
        ([3, 6, 1, 3, 4], [2, 1, 3, 4, 5], 25, 3),
        ([11, 12, 19], [10, 8, 7], 19, 0),
        (
            [
                19,
                63,
                21,
                8,
                5,
                46,
                56,
                45,
                54,
                30,
                92,
                63,
                31,
                71,
                87,
                94,
                67,
                8,
                19,
                89,
                79,
                25,
            ],
            [
                91,
                92,
                39,
                89,
                62,
                81,
                33,
                99,
                28,
                99,
                86,
                19,
                5,
                6,
                19,
                94,
                65,
                86,
                17,
                10,
                8,
                42,
            ],
            85,
            1,
        ),
    ],
)
def test_solution(charge_times, running_costs, budget, expected):
    assert (
        Solution().maximumRobots(charge_times, running_costs, budget)
        == expected
    )
