class Solution:
    def minWindow(self, s: str, t: str) -> str:
        result: tuple[int, int] = (0, -1)
        result_len = len(s) + 1

        t_char_count: dict[str, int] = {}
        for x in t:
            t_char_count[x] = t_char_count.get(x, 0) + 1

        window: dict[str, int] = {}

        have = 0
        need = len(t_char_count)

        left_i = 0
        while left_i < len(s) and s[left_i] not in t_char_count:
            left_i += 1

        for right_i in range(left_i, len(s)):
            right = s[right_i]

            if right in t_char_count:
                window[right] = window.get(right, 0) + 1

                if window[right] == t_char_count[right]:
                    have += 1

            while have == need:
                if (length := right_i - left_i + 1) < result_len:
                    result_len = length
                    result = (left_i, right_i)

                left = s[left_i]

                if left in t_char_count:
                    window[left] -= 1

                    if window[left] < t_char_count[left]:
                        have -= 1

                left_i += 1

        left_i, right_i = result
        return s[left_i : right_i + 1]
