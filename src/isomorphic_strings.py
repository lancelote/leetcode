class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        taken: set[str] = set()
        translation: dict[str, str] = {}

        for a, b in zip(s, t):
            if a not in translation:
                if b in taken:
                    return False

                translation[a] = b
                taken.add(b)
            elif translation[a] != b:
                return False

        return True
