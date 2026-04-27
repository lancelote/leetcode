class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        left = 0
        char_to_idx: dict[str, int] = {}

        for right in range(len(s)):
            x = s[right]

            if x in char_to_idx:
                left = max(left, char_to_idx[x])

            max_length = max(max_length, right - left + 1)
            char_to_idx[x] = right + 1

        return max_length
