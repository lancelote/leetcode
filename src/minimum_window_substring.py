class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        window: dict[str, int] = {}
        t_counts: dict[str, int] = {}
        for char in t:
            t_counts[char] = t_counts.get(char, 0) + 1

        have = 0
        need = len(t_counts)
        left_i = 0
        result = (-1, -1)
        result_len = float("infinity")

        for right_i, right_char in enumerate(s):
            window[right_char] = window.get(right_char, 0) + 1

            if (
                right_char in t_counts
                and window[right_char] == t_counts[right_char]
            ):
                have += 1

            while have == need:
                if (window_size := right_i - left_i + 1) < result_len:
                    result = (left_i, right_i)
                    result_len = window_size

                left_char = s[left_i]
                window[left_char] -= 1
                if (
                    left_char in t_counts
                    and window[left_char] < t_counts[left_char]
                ):
                    have -= 1
                left_i += 1

        left, right = result
        return s[left : right + 1]
