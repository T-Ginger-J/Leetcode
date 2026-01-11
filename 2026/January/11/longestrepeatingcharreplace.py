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

