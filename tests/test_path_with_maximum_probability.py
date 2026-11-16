import pytest

from src.path_with_maximum_probability import Solution


@pytest.mark.parametrize(
    "n,edges,succ_prob,start_node,end_node,expected",
    (
        (
            3,
            [[0, 1], [1, 2], [0, 2]],
            [0.5, 0.5, 0.2],
            0,
            2,
            0.25,
        ),
        (
            3,
            [[0, 1], [1, 2], [0, 2]],
            [0.5, 0.5, 0.3],
            0,
            2,
            0.3,
        ),
        (
            3,
            [[0, 1]],
            [0.5],
            0,
            2,
            0.0,
        ),
    ),
)
def test_solution(n, edges, succ_prob, start_node, end_node, expected):
    assert (
        Solution().maxProbability(
            n,
            edges,
            succ_prob,
            start_node,
            end_node,
        )
        == expected
    )
