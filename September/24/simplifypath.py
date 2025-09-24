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
    
    def simplifyPathFilter(self, path: str) -> str:
        stack = []
        for p in [p for p in path.split("/") if p not in ["", "."]]:
            if p == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(p)
        return "/" + "/".join(stack)
    
    simplifyPathOneLine=lambda s,p:"/"+"/".join(__import__('functools').reduce(lambda st,x:st[:-1] if x==".."and st else st+[x],filter(lambda y:y not in["","."],p.split("/")),[]))

# Example usage:
# sol = Solution()
# print(sol.simplifyPath("/home/"))       # "/home"
# print(sol.simplifyPath("/../"))         # "/"
# print(sol.simplifyPath("/home//foo/"))  # "/home/foo"
