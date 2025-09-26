# LeetCode 76: Minimum Window Substring
# Explanation:
# 1. Use sliding window technique with two pointers (l, r).
# 2. Expand r to include chars until window contains all t.
# 3. Shrink l to minimize window while still valid.
# Time Complexity: O(|s| + |t|)
# Space Complexity: O(|s| + |t|)

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        need = Counter(t)
        have = {}
        required, formed = len(need), 0
        res, res_len = [-1, -1], float("inf")
        l = 0
        
        for r, char in enumerate(s):
            have[char] = have.get(char, 0) + 1
            if char in need and have[char] == need[char]:
                formed += 1
            
            while formed == required:
                if (r - l + 1) < res_len:
                    res, res_len = [l, r], r - l + 1
                have[s[l]] -= 1
                if s[l] in need and have[s[l]] < need[s[l]]:
                    formed -= 1
                l += 1
        
        l, r = res
        return s[l:r+1] if res_len != float("inf") else ""

# Example usage:
# sol = Solution()
# print(sol.minWindow("ADOBECODEBANC", "ABC"))  # "BANC"
# print(sol.minWindow("a", "a"))                # "a"
# print(sol.minWindow("a", "aa"))               # ""
