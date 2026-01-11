# LeetCode 424: Longest Repeating Character Replacement
# Explanation:
# 1. Use sliding window technique to maintain a substring where at most k characters 
#    can be replaced to make all characters the same.
# 2. Maintain a frequency map of characters in the current window.
# 3. Track the count of the most frequent character in the window (`max_count`).
# 4. If current window size minus `max_count` > k, shrink the window from left.
# 5. Keep updating the maximum window size found.

from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = Counter()
        left = 0
        max_count = 0
        result = 0
        
        for right in range(len(s)):
            count[s[right]] += 1
            max_count = max(max_count, count[s[right]])
            
            # If more than k replacements are needed, shrink window
            while (right - left + 1) - max_count > k:
                count[s[left]] -= 1
                left += 1
            
            result = max(result, right - left + 1)
        
        return result

# Example 1
s = "ABAB"
k = 2
# Output: 4 (replace two 'A's or 'B's to make all same)
print(Solution().characterReplacement(s, k))

# Example 2
s = "AABABBA"
k = 1
# Output: 4 ("ABBB" or "AABA")
print(Solution().characterReplacement(s, k))
