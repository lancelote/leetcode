import pytest

from src.range_product_queries_of_powers import Solution


@pytest.mark.parametrize(
    "n,queries,expected",
    [
        (15, [[0, 1], [2, 2], [0, 3]], [2, 4, 64]),
        (2, [[0, 0]], [2]),
        (
            53,
            [
                [2, 3],
                [0, 1],
                [0, 1],
                [0, 1],
                [0, 0],
                [0, 3],
                [3, 3],
                [2, 3],
                [1, 1],
                [2, 3],
            ],
            [512, 4, 4, 4, 1, 2048, 32, 512, 4, 512],
        ),
    ],
)
def test_solution(n, queries, expected):
    assert Solution().productQueries(n, queries) == expected
