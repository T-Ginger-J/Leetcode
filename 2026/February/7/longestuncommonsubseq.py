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

    # -------------------------------------------------------
    # Default Method
    # -------------------------------------------------------
    def findLUSlength(self, a: str, b: str) -> int:
        return self.findLUSlength(a, b)


# -------------------------------------------------------
# Examples (Including Edge Cases)
# -------------------------------------------------------

# Example 1
print(Solution().findLUSlength("aba", "cdc"))   # 3

# Example 2
print(Solution().findLUSlength("aaa", "aaa"))   # -1

# Example 3 (Different Lengths)
print(Solution().findLUSlength("abcd", "ab"))   # 4

# Example 4 (One Empty String)
print(Solution().findLUSlength("", "abc"))      # 3

# Example 5 (Single Character)
print(Solution().findLUSlength("a", "b"))       # 1
