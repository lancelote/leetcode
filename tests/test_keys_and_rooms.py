import pytest

from src.keys_and_rooms import Solution


@pytest.mark.parametrize(
    "rooms,expected",
    (
        ([[1], [2], [3], []], True),
        ([[1, 3], [3, 0, 1], [2], [0]], False),
    ),
)
def test_solution(rooms, expected):
    assert Solution().canVisitAllRooms(rooms) == expected
