def is_valid(subseq: list[str], stamp: str) -> bool:
    result = False
    for i in range(len(subseq)):
        if subseq[i] == "?":
            continue
        elif subseq[i] != stamp[i]:
            return False
        elif subseq[i] == stamp[i]:
            result = True
    return result


class Solution:
    def movesToStamp(self, stamp: str, target: str) -> list[int]:
        result = []
        todo = len(target)
        target_list = list(target)

        while todo:
            proceed = False

            for i in range(len(target) - len(stamp) + 1):
                if is_valid(target_list[i : i + len(stamp)], stamp):
                    proceed = True
                    result.append(i)

                    for j in range(len(stamp)):
                        if target_list[i + j] != "?":
                            target_list[i + j] = "?"
                            todo -= 1
                    break

            if not proceed:
                return []

        return result[::-1]
