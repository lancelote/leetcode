import collections


class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        max_score = 0
        cur_score = 0

        deque = collections.deque(sorted(tokens))

        while deque and cur_score >= 0:
            if deque[0] <= power:
                power -= deque.popleft()
                cur_score += 1
            else:
                power += deque.pop()
                cur_score -= 1

            max_score = max(max_score, cur_score)

        return max_score
