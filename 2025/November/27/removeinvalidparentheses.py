# LeetCode 301: Remove Invalid Parentheses
# Explanation:
# 1. Use BFS to generate all possible strings by removing one parenthesis at a time.
# 2. Stop at the first level where we find valid strings.
# 3. Use a set to avoid duplicates.
# Time Complexity: O(2^n * n), generating all combinations and checking validity
# Space Complexity: O(2^n), storing all visited strings

from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str):
        if not s: return [""]
        
        def is_valid(string):
            count = 0
            for c in string:
                if c == '(':
                    count += 1
                elif c == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        visited = set([s])
        queue = deque([s])
        found = False
        res = []
        
        while queue:
            level_size = len(queue)
            level_seen = set()
            for _ in range(level_size):
                curr = queue.popleft()
                if is_valid(curr):
                    res.append(curr)
                    found = True
                if found:
                    continue
                for i in range(len(curr)):
                    if curr[i] not in '()':
                        continue
                    next_str = curr[:i] + curr[i+1:]
                    if next_str not in visited:
                        queue.append(next_str)
                        visited.add(next_str)
            if found:
                break
        return res

    def removeInvalidParenthesesDFS(self, s: str):
        res = set()
        
        def dfs(s, start, lremove, rremove):
            if lremove == 0 and rremove == 0:
                if self.is_valid(s):
                    res.add(s)
                return
            for i in range(start, len(s)):
                if i != start and s[i] == s[i-1]:
                    continue
                if lremove + rremove > len(s) - i:
                    return
                if lremove > 0 and s[i] == '(':
                    dfs(s[:i]+s[i+1:], i, lremove-1, rremove)
                if rremove > 0 and s[i] == ')':
                    dfs(s[:i]+s[i+1:], i, lremove, rremove-1)
        
        lremove = rremove = 0
        for c in s:
            if c == '(': lremove += 1
            elif c == ')':
                if lremove > 0: lremove -= 1
                else: rremove += 1
        dfs(s, 0, lremove, rremove)
        return list(res)
    
    def is_valid(self, s):
        count = 0
        for c in s:
            if c == '(': count += 1
            elif c == ')': count -= 1
            if count < 0: return False
        return count == 0
    
s = "()())()"
print(Solution().removeInvalidParentheses(s))  # ["()()()", "(())()"]

s = "(a)())()"
print(Solution().removeInvalidParentheses(s))  # ["(a)()()", "(a())()"]

s = ")("
print(Solution().removeInvalidParentheses(s))  # [""]
