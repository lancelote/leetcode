import pytest

from src.distribute_money_to_maximum_children import Solution


@pytest.mark.parametrize(
    "money,children,expected",
    [
        (20, 3, 1),
        (16, 2, 2),
        (7, 1, 0),
        (16, 1, 0),
        (1, 2, -1),
        (4, 2, 0),
        (8, 2, 0),
        (16, 3, 1),
        (9, 3, 0),
        (16, 10, 0),
        (17, 2, 1),
        (9, 2, 1),
        (17, 10, 1),
        (18, 11, 1),
    ],
)
def test_solution(money, children, expected):
    assert Solution().distMoney(money, children) == expected
