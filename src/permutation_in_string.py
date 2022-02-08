def to_int(char: str) -> int:
    return ord(char) - ord("a")


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_counter = [0] * 26
        s2_counter = [0] * 26

        for x1, x2 in zip(s1, s2):
            s1_counter[to_int(x1)] += 1
            s2_counter[to_int(x2)] += 1

        similar = sum(c1 == c2 for c1, c2 in zip(s1_counter, s2_counter))

        left = 0
        for right in range(len(s1), len(s2)):
            if similar == 26:
                return True

            new = to_int(s2[right])
            s2_counter[new] += 1

            if s1_counter[new] == s2_counter[new]:
                similar += 1
            elif s1_counter[new] + 1 == s2_counter[new]:
                similar -= 1

            old = to_int(s2[left])
            s2_counter[old] -= 1

            if s1_counter[old] == s2_counter[old]:
                similar += 1
            elif s1_counter[old] - 1 == s2_counter[old]:
                similar -= 1

            left += 1

        return similar == 26
