class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_chars: dict[str, int] = {}
        t_chars: dict[str, int] = {}

        for i in range(len(s)):
            s_chars[s[i]] = s_chars.get(s[i], 0) + 1
            t_chars[t[i]] = t_chars.get(t[i], 0) + 1

        for k, v in s_chars.items():
            if k not in t_chars:
                return False

            if t_chars[k] != v:
                return False

            del t_chars[k]

        return len(t_chars) == 0
