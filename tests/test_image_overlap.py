import pytest

from src.image_overlap import Solution


@pytest.mark.parametrize(
    "img1,img2,expected",
    [
        (
            [[1, 1, 0], [0, 1, 0], [0, 1, 0]],
            [[0, 0, 0], [0, 1, 1], [0, 0, 1]],
            3,
        ),
        ([[1]], [[1]], 1),
        ([[0]], [[0]], 0),
    ],
)
def test_solution(img1, img2, expected):
    assert Solution().largestOverlap(img1, img2) == expected
