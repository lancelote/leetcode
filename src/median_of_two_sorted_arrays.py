from collections.abc import Iterator


def get_item(nums1: list[int], nums2: list[int]) -> Iterator[int]:
    n = len(nums1)
    m = len(nums2)

    i1 = i2 = 0

    for _ in range(n + m):
        if i1 == n:
            yield nums2[i2]
            i2 += 1
        elif i2 == m:
            yield nums1[i1]
            i1 += 1
        elif nums1[i1] > nums2[i2]:
            yield nums2[i2]
            i2 += 1
        else:
            yield nums1[i1]
            i1 += 1


class Solution:
    def findMedianSortedArrays(
        self, nums1: list[int], nums2: list[int]
    ) -> float:
        n = len(nums1)
        m = len(nums2)

        if not n and not m:
            return 0

        iter0 = get_item(nums1, nums2)

        if (n + m) % 2 == 0:
            a = b = next(iter0)

            for _ in range((n + m) // 2):
                a = b
                b = next(iter0)

            return (a + b) / 2

        else:
            a = 0

            for _ in range((n + m) // 2 + 1):
                a = next(iter0)

            return a
