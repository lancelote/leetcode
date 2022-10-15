class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        chars: list[str] = []
        freqs: list[int] = []

        def find_min(i: int, left_k: int, same_chars: int = 0) -> int:
            if same_chars == 0 and dp[i][left_k] != -1:
                return dp[i][left_k]

            cur_count = same_chars + freqs[i]

            min_len = (
                1
                + min(len(str(cur_count)), cur_count - 1)
                + find_min(i + 1, left_k)
            )

            for leave_count, code_count in [(0, 0), (1, 1), (9, 2), (99, 3)]:
                if (
                    cur_count > leave_count
                    and left_k >= cur_count - leave_count
                ):
                    min_len = min(
                        min_len,
                        code_count
                        + find_min(i + 1, left_k - (cur_count - leave_count)),
                    )

            try:
                next_i = chars.index(chars[i], i + 1)
            except ValueError:
                next_i = -1
            delete_count = sum(freqs[i + 1 : next_i])
            if next_i > 0 and left_k >= delete_count:
                min_len = min(
                    min_len, find_min(next_i, left_k - delete_count, cur_count)
                )

            if same_chars == 0:
                dp[i][left_k] = min_len

            return min_len

        for x in s:
            if not chars or x != chars[-1]:
                chars.append(x)
                freqs.append(0)
            freqs[-1] += 1

        dp: list[list[int]] = [[-1] * (k + 1) for _ in range(len(freqs))]
        dp += [[0] * (k + 1)]

        return find_min(0, k)
