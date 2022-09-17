import pytest

from src.maximum_matching_of_players_with_trainers import Solution


@pytest.mark.parametrize(
    "players,trainers,expected_matches",
    [
        ([4, 7, 9], [8, 2, 5, 8], 2),
        ([1, 1, 1], [10], 1),
        ([10], [1], 0),
    ],
)
def test_solution(players, trainers, expected_matches):
    assert (
        Solution().matchPlayersAndTrainers(players, trainers)
        == expected_matches
    )
