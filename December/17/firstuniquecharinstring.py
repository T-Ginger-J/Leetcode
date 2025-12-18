# LeetCode 387: First Unique Character in a String
# Explanation:
# 1. Count frequency of each character.
# 2. Return index of first character with count 1.
# Time Complexity: O(n)
# Space Complexity: O(1) for 26 lowercase letters

from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        for i, ch in enumerate(s):
            if count[ch] == 1:
                return i
        return -1

print(Solution().firstUniqChar("leetcode"))  # Output: 0 ('l' is first unique)
print(Solution().firstUniqChar("loveleetcode"))  # Output: 2 ('v' is first unique)
print(Solution().firstUniqChar("aabb"))  # Output: -1 (no unique char)
