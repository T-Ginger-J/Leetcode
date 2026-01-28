# LeetCode 482: License Key Formatting
# Explanation:
# Given a string s representing a license key and an integer k,
# reformat the string so that:
# 1. All letters are uppercase.
# 2. The string is split into groups of size k, separated by dashes.
# 3. The first group may be shorter than k, but all others must be exactly k.
# 4. Original dashes are removed before regrouping.
#
# Method 1: Reverse Traversal (Optimal)
# - Remove dashes and uppercase the string.
# - Build the result from right to left inserting dashes every k characters.
#
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()
        res = []
        count = 0

        for ch in reversed(s):
            if count == k:
                res.append("-")
                count = 0
            res.append(ch)
            count += 1

        return "".join(reversed(res))


