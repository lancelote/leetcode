import string


class Solution:
    def minDeletions(self, s: str) -> int:
        result = 0
        seen = {0}

        for x in string.ascii_lowercase:
            count = s.count(x)

            while count and count in seen:
                count -= 1
                result += 1

            seen.add(count)

        return result
