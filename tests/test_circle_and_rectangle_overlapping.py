import pytest

from src.circle_and_rectangle_overlapping import Solution


@pytest.mark.parametrize(
    "r,x,y,x1,y1,x2,y2,expected",
    (
        (1, 0, 0, 1, -1, 3, 1, True),
        (1, 1, 1, 1, -3, 2, -1, False),
        (1, 0, 0, -1, 0, 0, 1, True),
        (1206, -5597, -276, -5203, -1795, -4648, 1721, True),
    ),
)
def test_solution(r, x, y, x1, y1, x2, y2, expected):
    assert Solution().checkOverlap(r, x, y, x1, y1, x2, y2) is expected
