class Solution:
    def simplifyPath(self, path: str) -> str:
        stack: list[str] = []

        for part in path.strip("/").split("/"):
            if part == "..":
                if stack:
                    stack.pop()
            elif part and part != ".":
                stack.append(part)

        return "/" + "/".join(stack)
