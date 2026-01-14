class Solution:
    def buildArray(self, target: list[int], _: int) -> list[str]:
        stream = 1
        stack: list[int] = []
        ops: list[str] = []

        while not stack or len(stack) != len(target):
            stack.append(stream)
            ops.append("Push")

            if stack[-1] != target[len(stack) - 1]:
                stack.pop()
                ops.append("Pop")

            stream += 1

        return ops
