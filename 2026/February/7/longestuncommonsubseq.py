# LeetCode 521: Longest Uncommon Subsequence I
# Explanation:
# 1. We are given two strings a and b.
# 2. The longest uncommon subsequence is the longest string that is a subsequence
#    of one string but NOT the other.
# 3. If a == b, no uncommon subsequence exists.
# 4. Otherwise, the longer string itself is the answer.

# Key Observation:
# - If a != b, the longer string cannot be a subsequence of the shorter one
#   (or even if equal length but different, one is not subsequence of the other).

# Methods Used:
# - Direct Comparison (Greedy Observation)
# - Subsequence Check (Generalized Reasoning)

# Time Complexity:
# - O(n)

# Space Complexity:
# - O(1)


class Solution:

    # -------------------------------------------------------
    # Method 1: Direct Observation (Optimal)
    # -------------------------------------------------------
    def findLUSlength(self, a: str, b: str) -> int:

        if a == b:
            return -1

        return max(len(a), len(b))

