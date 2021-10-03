class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        result = 0

        for operation in operations:
            if operation.startswith("--") or operation.endswith("--"):
                result -= 1
            else:
                result += 1

        return result
