def isBadVersion(version: int) -> int:
    return 1 if version >= 4 else 0


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n

        while left < right:
            middle = left + (right - left) // 2
            is_bad = isBadVersion(middle)

            if is_bad:
                right = middle
            else:
                left = middle + 1

        return right
