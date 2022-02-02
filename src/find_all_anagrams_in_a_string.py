Counter = dict[str, int]


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(s) < len(p):
            return []

        p_count: Counter = {}
        s_count: Counter = {}

        for i in range(len(p)):
            p_count[p[i]] = 1 + p_count.get(p[i], 0)
            s_count[s[i]] = 1 + s_count.get(s[i], 0)

        result = [0] if p_count == s_count else []

        left = 0
        for right in range(len(p), len(s)):
            s_count[s[left]] -= 1
            s_count[s[right]] = 1 + s_count.get(s[right], 0)

            if s_count[s[left]] == 0:
                s_count.pop(s[left])

            left += 1

            if p_count == s_count:
                result.append(left)

        return result
