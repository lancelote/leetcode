class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack: list[int] = []

        for x in asteroids:
            if not stack or (x < 0) is (stack[-1] < 0):
                stack.append(x)
            else:
                while stack:
                    if x > 0:
                        stack.append(x)
                        break

                    if x < 0 < stack[-1]:
                        if abs(stack[-1]) < abs(x):
                            stack.pop()
                        elif abs(stack[-1]) == abs(x):
                            stack.pop()
                            break
                        else:
                            break
                    else:
                        stack.append(x)
                        break
                else:
                    stack.append(x)

        return stack
