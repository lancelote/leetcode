class Solution:
    def findArray(self, pref: list[int]) -> list[int]:
        rolling = pref[0]
        res = [pref[0]]

        for i in range(1, len(pref)):
            new_x = rolling ^ pref[i]
            rolling ^= new_x
            res.append(new_x)

        return res
