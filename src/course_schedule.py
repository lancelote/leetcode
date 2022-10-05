from collections import defaultdict


class Solution:
    def canFinish(self, num_courses: int, prereqs: list[list[int]]) -> bool:
        course_to_prereqs: dict[int, list[int]] = defaultdict(list)

        for course, prereq in prereqs:
            course_to_prereqs[course].append(prereq)

        seen: set[int] = set()

        def dfs(course: int) -> bool:
            if course in seen:
                return False
            if not course_to_prereqs[course]:
                return True

            seen.add(course)

            for prereq in course_to_prereqs[course]:
                if not dfs(prereq):
                    return False

            seen.remove(course)

            course_to_prereqs[course] = []
            return True

        for course in range(num_courses):
            if not dfs(course):
                return False

        return True
