import pytest

from src.rectangle_area import Solution


@pytest.mark.parametrize(
    "args,expected",
    [
        ((-3, 0, 3, 4, 0, -1, 9, 2), 45),
        ((-2, -2, 2, 2, -2, -2, 2, 2), 16),
    ],
)
def test_solution(args, expected):
    assert Solution().computeArea(*args) == expected
