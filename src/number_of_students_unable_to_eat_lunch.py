from collections import deque


class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        students_deque = deque(students)
        sandwiches_deque = deque(sandwiches)

        while True:
            start_len = len(students_deque)

            for _ in range(len(students_deque)):
                student = students_deque.popleft()

                if student != sandwiches_deque[0]:
                    students_deque.append(student)
                else:
                    sandwiches_deque.popleft()

            if start_len == len(students_deque):
                break

        return len(students_deque)
