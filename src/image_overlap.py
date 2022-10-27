from typing import TypeAlias

Image: TypeAlias = list[list[int]]


def overlap(img1: Image, img2: Image, dx: int, dy: int) -> int:
    n = len(img1)
    left_shift_count = 0
    right_shift_count = 0

    for y2, y1 in enumerate(range(dy, n)):
        for x2, x1 in enumerate(range(dx, n)):
            if img1[y1][x1] == img2[y2][x2] == 1:
                left_shift_count += 1
            if img1[y1][x2] == img2[y2][x1] == 1:
                right_shift_count += 1

    return max(left_shift_count, right_shift_count)


class Solution:
    def largestOverlap(self, img1: Image, img2: Image) -> int:
        n = len(img1)
        max_overlap = 0

        for dy in range(n):
            for dx in range(n):
                max_overlap = max(max_overlap, overlap(img1, img2, dx, dy))
                max_overlap = max(max_overlap, overlap(img2, img1, dx, dy))

        return max_overlap
