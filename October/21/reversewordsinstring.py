# LeetCode 151: Reverse Words in a String
# Explanation:
# 1. Split the input string by whitespace to separate words.
# 2. Reverse the order of the words.
# 3. Join them back together with a single space.
# 4. Handles multiple spaces and trimming automatically via split().
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])

print(Solution().reverseWords("the sky is blue"))
# Output: "blue is sky the"

print(Solution().reverseWords("  hello world  "))
# Output: "world hello"

print(Solution().reverseWords("a good   example"))
# Output: "example good a"
