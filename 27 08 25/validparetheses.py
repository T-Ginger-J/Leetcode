# O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {'(': ')', '{': '}', '[': ']'}
        
        for char in s:
            if char in mapping:  # opening bracket
                stack.append(mapping[char])
            else:  # closing bracket
                if not stack or stack.pop() != char:
                    return False
        return not stack
    
