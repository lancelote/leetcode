import pytest

from src.minimum_number_of_moves_to_seat_everyone import Solution


@pytest.mark.parametrize(
    "seats,students,expected",
    [
        ([3, 1, 5], [2, 7, 4], 4),
        ([4, 1, 5, 9], [1, 3, 2, 6], 7),
        ([2, 2, 6, 6], [1, 3, 2, 6], 4),
        ([12, 14, 19, 19, 12], [19, 2, 17, 20, 7], 19),
    ],
)
def test_solution(seats, students, expected):
    assert Solution().minMovesToSeat(seats, students) == expected
