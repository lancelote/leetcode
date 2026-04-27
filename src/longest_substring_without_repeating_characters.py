class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        left = right = 0
        seen: set[str] = set()

        while right < len(s):
            x = s[right]

            while x in seen:
                seen.remove(s[left])
                left += 1

            seen.add(x)
            max_length = max(max_length, right - left + 1)
            right += 1

        return max_length
