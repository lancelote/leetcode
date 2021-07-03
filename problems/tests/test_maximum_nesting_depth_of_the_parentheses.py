import pytest
from src.maximum_nesting_depth_of_the_parentheses import Solution


@pytest.mark.parametrize(
    "text,depth",
    [
        ("(1+(2*3)+((8)/4))+1", 3),
        ("(1)+((2))+(((3)))", 3),
        ("1+(2*3)/(2-1)", 1),
        ("1", 0),
    ],
)
def test_max_depth(text, depth):
    assert Solution().maxDepth(text) == depth
