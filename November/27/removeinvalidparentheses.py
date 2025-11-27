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
