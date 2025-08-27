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
    
    def isValidOneLine(self, s: str) -> bool:
        stack = []
        mapping = {'(': ')', '{': '}', '[': ']'}
        return all(stack.append(mapping[c]) if c in mapping else stack.pop() == c for c in s) and not stack

# Example usage
sol = Solution()
print(sol.isValid("()"))        # True
print(sol.isValid("()[]{}"))    # True
print(sol.isValid("(]"))        # False
print(sol.isValid("([)]"))      # False
print(sol.isValid("{[]}"))      # True
