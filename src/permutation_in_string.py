class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_counter: dict[str, int] = {}
        s2_counter: dict[str, int] = {}

        for i in range(len(s1)):
            x1 = s1[i]
            x2 = s2[i]

            s1_counter[x1] = 1 + s1_counter.get(x1, 0)
            s2_counter[x2] = 1 + s2_counter.get(x2, 0)

        if s1_counter == s2_counter:
            return True

        for i in range(len(s1), len(s2)):
            to_remove = s2[i - len(s1)]
            to_add = s2[i]

            s2_counter[to_remove] -= 1
            if s2_counter[to_remove] == 0:
                del s2_counter[to_remove]
            s2_counter[to_add] = 1 + s2_counter.get(to_add, 0)

            if s1_counter == s2_counter:
                return True

        return False
