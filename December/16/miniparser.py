# LeetCode 385: Mini Parser
# Explanation:
# 1. Use stack to keep track of NestedInteger objects.
# 2. Handle digits, negative signs, '[' and ']' carefully.
# Time Complexity: O(n)
# Space Complexity: O(d)

class NestedInteger:
    def __init__(self, val=None):
        self.integer = val
        self.list = [] if val is None else None

    def isInteger(self):
        return self.integer is not None

    def add(self, elem):
        if self.list is not None:
            self.list.append(elem)

    def setInteger(self, val):
        self.integer = val
        self.list = None

    def getInteger(self):
        return self.integer

    def getList(self):
        return self.list

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if not s.startswith('['):
            return NestedInteger(int(s))
        
        stack = []
        num = ''
        negative = False
        
        for i, ch in enumerate(s):
            if ch == '-':
                negative = True
            elif ch.isdigit():
                num += ch
            elif ch == '[':
                stack.append(NestedInteger())
            elif ch in ',]':
                if num:
                    n = int(num) * (-1 if negative else 1)
                    stack[-1].add(NestedInteger(n))
                    num = ''
                    negative = False
                if ch == ']' and len(stack) > 1:
                    ni = stack.pop()
                    stack[-1].add(ni)
        return stack[0]
    
