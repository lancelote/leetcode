class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        def scan(left: int, right: int) -> None:
            nonlocal count

            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

        for i in range(n):
            scan(i, i)
            scan(i, i + 1)

        return count
