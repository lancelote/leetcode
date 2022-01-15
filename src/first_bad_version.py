def isBadVersion(version: int) -> int:
    return 1 if version >= 4 else 0


class Solution:
    def firstBadVersion(self, n: int) -> int:
        oldest = 1
        newest = n

        while oldest < newest:
            version = oldest + (newest - oldest) // 2

            if isBadVersion(version):
                newest = version
            else:
                oldest = version + 1

        return newest
