import pytest

from src.bag_of_tokens import Solution


@pytest.mark.parametrize(
    "tokens,power,expected_max_score",
    [
        ([100], 50, 0),
        ([100, 200], 150, 1),
        ([100, 200, 300, 400], 200, 2),
    ],
)
def test_solution(tokens, power, expected_max_score):
    assert Solution().bagOfTokensScore(tokens, power) == expected_max_score
