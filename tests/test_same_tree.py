import pytest

from src.same_tree import Solution
from src.utils.binary_tree import list_to_tree


@pytest.mark.parametrize(
    "list_p,list_q,equal",
    [
        ([1, 2, 3], [1, 2, 3], True),
        ([1, 2], [1, None, 2], False),
        ([], [], True),
        ([1, 2, 1], [1, 1, 2], False),
    ],
)
def test_solution(list_p, list_q, equal):
    p = list_to_tree(list_p)
    q = list_to_tree(list_q)

    assert Solution().isSameTree(p, q) is equal
