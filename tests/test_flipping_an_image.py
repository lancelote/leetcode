import pytest

from src.flipping_an_image import Solution


@pytest.mark.parametrize(
    "image,output",
    [
        ([[1, 1, 0], [1, 0, 1], [0, 0, 0]], [[1, 0, 0], [0, 1, 0], [1, 1, 1]]),
        (
            [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]],
            [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]],
        ),
    ],
)
def test_solution(image, output):
    assert Solution().flipAndInvertImage(image) == output
