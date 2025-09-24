# LeetCode 71: Simplify Path
# Explanation:
# 1. Split path by '/'.
# 2. Use a stack to build valid directories.
# 3. Skip '.' and empty parts, pop for '..'.
# 4. Join stack with '/'.
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for part in path.split("/"):
            if part == "" or part == ".":
                continue
            elif part == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(part)
        return "/" + "/".join(stack)
