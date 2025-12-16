# LeetCode 383: Ransom Note
# Explanation:
# 1. Count letters in magazine.
# 2. Check if ransomNote can be formed.
# Time Complexity: O(n + m)
# Space Complexity: O(26)

from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = Counter(magazine)
        for ch in ransomNote:
            if count[ch] <= 0:
                return False
            count[ch] -= 1
        return True

print(Solution().canConstruct("a", "b"))         # Output: False
print(Solution().canConstruct("aa", "ab"))       # Output: False
print(Solution().canConstruct("aa", "aab"))      # Output: True
