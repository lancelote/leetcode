class Solution:
    def fullBloomFlowers(
        self, flowers: list[list[int]], people: list[int]
    ) -> list[int]:
        starts = sorted([x for [x, _] in flowers], reverse=True)
        ends = sorted([x for [_, x] in flowers], reverse=True)
        folks = sorted([(x, i) for i, x in enumerate(people)], reverse=True)

        count = 0
        result: list[int] = [0] * len(people)

        while folks:
            if not ends:
                _, person_id = folks.pop()
                result[person_id] = count
            elif starts and starts[-1] <= folks[-1][0]:
                starts.pop()
                count += 1
            elif ends[-1] < folks[-1][0]:
                ends.pop()
                count -= 1
            else:
                _, person_id = folks.pop()
                result[person_id] = count

        return result
