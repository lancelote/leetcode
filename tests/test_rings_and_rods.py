import pytest

from src.rings_and_rods import Solution


@pytest.mark.parametrize(
    "rings,count",
    [
        ("B0B6G0R6R0R6G9", 1),
        ("B0R0G0R9R0B0G0", 1),
        ("G4", 0),
    ],
)
def test_solution(rings, count):
    assert Solution().countPoints(rings) == count
