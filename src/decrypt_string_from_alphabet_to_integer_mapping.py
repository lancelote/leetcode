def get_mapping() -> dict[str, str]:
    mapping = {}

    for i, ch in enumerate("abcdefghi", start=1):
        mapping[str(i)] = ch

    for i, ch in enumerate("jklmnopqrstuvwxyz", start=10):
        mapping[f"{i}#"] = ch

    return mapping


class Solution:
    def freqAlphabets(self, s: str) -> str:
        mapping = get_mapping()
        result = []

        i = 0

        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == "#":
                code = s[i] + s[i + 1] + "#"
                i += 3
            else:
                code = str(s[i])
                i += 1
            result.append(mapping[code])

        return "".join(result)
