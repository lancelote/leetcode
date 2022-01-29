def isBadVersion(version: int) -> int:
    return 1 if version >= 4 else 0


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n

        while left < right:
            middle = left + (right - left) // 2

            if isBadVersion(middle):
                right = middle
            else:
                left = middle + 1

        return right
