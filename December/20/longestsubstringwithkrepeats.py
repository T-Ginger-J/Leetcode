# LeetCode 395: Longest Substring with At Least K Repeating Characters
# Explanation:
# 1. Split string at chars that appear less than k times
# 2. Recursively find the max length in each segment
# Time Complexity: O(n)
# Space Complexity: O(26) recursion

from collections import Counter

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        count = Counter(s)
        for ch in count:
            if count[ch] < k:
                return max(self.longestSubstring(sub, k) for sub in s.split(ch))
        return len(s)

print(Solution().longestSubstring("aaabb", 3))       # Output: 3 ("aaa")
print(Solution().longestSubstring("ababbc", 2))      # Output: 5 ("ababb")
print(Solution().longestSubstring("ababacb", 3))     # Output: 0
