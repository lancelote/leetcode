import pytest

from src.gas_station import Solution


@pytest.mark.parametrize(
    "expected,gas,cost",
    (
        (3, [1, 2, 3, 4, 5], [3, 4, 5, 1, 2]),
        (-1, [2, 3, 4], [3, 4, 3]),
    ),
)
def test_solution(expected, gas, cost):
    assert expected == Solution().canCompleteCircuit(gas, cost)
