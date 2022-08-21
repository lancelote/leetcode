class Solution:
    def movesToStamp(self, stamp: str, target: str) -> list[int]:
        result = []
        turns = 0
        done = [False] * len(target)
        todo = len(target)

        while turns < 10 * len(target) and todo != 0:
            for i in range(len(target) - len(stamp) + 1):
                possible_stamp = False

                for j in range(len(stamp)):
                    if not done[i + j]:
                        possible_stamp = True
                    if target[i + j] != stamp[j] and not done[i + j]:
                        possible_stamp = False
                        break

                if possible_stamp:
                    for j in range(len(stamp)):
                        if not done[i + j]:
                            done[i + j] = True
                            todo -= 1
                    result.append(i)
                    break
            turns += 1

        return result[::-1] if turns < 10 * len(target) else []
