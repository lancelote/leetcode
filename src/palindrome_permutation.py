class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        chars: dict[str, int] = {}
        for x in s:
            chars[x] = chars.get(x, 0) + 1

        is_even = len(s) % 2 == 0
        for count in chars.values():
            if count % 2 != 0:
                if not is_even:
                    is_even = True
                else:
                    return False

        return True
