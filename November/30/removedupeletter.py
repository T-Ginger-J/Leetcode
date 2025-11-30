# LeetCode 316: Remove Duplicate Letters
# Explanation:
# 1. Goal: Return the smallest lexicographical string with unique letters.
# 2. Use a stack to build result:
#    - If current char is smaller than top and top occurs later, pop top.
#    - Push current char if not already in stack.
# 3. Use a counter for remaining occurrences.
# Time Complexity: O(n), each character pushed/popped at most once
# Space Complexity: O(26) for stack and seen set

from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = Counter(s)
        stack = []
        seen = set()
        for c in s:
            count[c] -= 1
            if c in seen:
                continue
            while stack and c < stack[-1] and count[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(c)
            seen.add(c)
        return ''.join(stack)

sol = Solution()
print(sol.removeDuplicateLetters("bcabc"))     # "abc"
print(sol.removeDuplicateLetters("cbacdcbc"))  # "acdb"
print(sol.removeDuplicateLetters("abacb"))     # "abc"
