# LeetCode 467: Unique Substrings in Wraparound String
# Explanation:
# The wraparound string is the infinite string:
#   "...abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz..."
#
# We are given a string p and must count how many unique non-empty substrings of p
# exist in the wraparound string.
#
# Method 1: Dynamic Programming on Characters (Optimal)
# - Let dp[c] be the length of the longest valid wraparound substring ending with char c.
# - Traverse p and keep track of the current consecutive wraparound length.
# - If p[i] follows p[i-1] in wraparound order, increment length; else reset to 1.
# - Update dp for the current character.
# - The answer is sum(dp.values()).
#
# Time Complexity: O(n)
# Space Complexity: O(1) (fixed alphabet size)

class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        dp = [0] * 26
        curr_len = 0

        for i in range(len(p)):
            if i > 0 and (ord(p[i]) - ord(p[i - 1]) == 1 or (p[i - 1] == 'z' and p[i] == 'a')):
                curr_len += 1
            else:
                curr_len = 1

            idx = ord(p[i]) - ord('a')
            dp[idx] = max(dp[idx], curr_len)

        return sum(dp)


# Additional Examples (Edge Cases and Non-LeetCode Examples)

sol = Solution()

# Example 1: Straight wraparound
print(sol.findSubstringInWraproundString("zab"))
# Expected output: 6
# Substrings: z, a, b, za, ab, zab

# Example 2: Repeated same character
print(sol.findSubstringInWraproundString("aaaa"))
# Expected output: 1
# Only "a" counts uniquely

# Example 3: Full alphabet
print(sol.findSubstringInWraproundString("abcdefghijklmnopqrstuvwxyz"))
# Expected output: 351
