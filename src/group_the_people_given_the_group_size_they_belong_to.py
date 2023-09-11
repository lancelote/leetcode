from collections import defaultdict


class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        result: list[list[int]] = []

        group_size_to_people: dict[int, list[int]] = defaultdict(list)

        for person, group_size in enumerate(groupSizes):
            if len(group_size_to_people[group_size]) < group_size:
                group_size_to_people[group_size].append(person)
            else:
                result.append(group_size_to_people[group_size])
                group_size_to_people[group_size].clear()
                group_size_to_people[group_size].append(person)

        for people in group_size_to_people.values():
            result.append(people)

        return result
