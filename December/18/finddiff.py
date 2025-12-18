# LeetCode 389: Find the Difference
# Explanation:
# 1. XOR all characters in s and t.
# 2. The result is the extra character.
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res = 0
        for ch in s + t:
            res ^= ord(ch)
        return chr(res)

print(Solution().findTheDifference("abcd", "abcde"))  # Output: "e"
print(Solution().findTheDifference("", "y"))         # Output: "y"
print(Solution().findTheDifference("a", "aa"))       # Output: "a"
