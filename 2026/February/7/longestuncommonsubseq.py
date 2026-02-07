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

    # -------------------------------------------------------
    # Method 2: Explicit Subsequence Check (Educational)
    # -------------------------------------------------------
    def findLUSlengthCheck(self, a: str, b: str) -> int:

        def isSubseq(s, t):
            i = 0
            for ch in t:
                if i < len(s) and s[i] == ch:
                    i += 1
            return i == len(s)

        if a == b:
            return -1

        if not isSubseq(a, b):
            return len(a)

        if not isSubseq(b, a):
            return len(b)

        return -1

