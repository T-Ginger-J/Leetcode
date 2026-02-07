# LeetCode 522: Longest Uncommon Subsequence II
# Explanation:
# 1. We are given a list of strings.
# 2. The longest uncommon subsequence is the longest string that is NOT
#    a subsequence of any other string in the list.
# 3. We must find the maximum length among all such valid strings.

# Methods Used:
# - Brute Force + Subsequence Checking
# - Sorting by Length (Greedy Pruning)

# Key Idea:
# - Sort strings by descending length.
# - For each string, check if it is a subsequence of any other string.
# - First valid one is the answer.

# Time Complexity:
# - O(n^2 * L)
#   n = number of strings, L = max string length

# Space Complexity:
# - O(1) (ignoring input storage)


from typing import List


class Solution:

    # -------------------------------------------------------
    # Method 1: Sort + Subsequence Check (Optimal)
    # -------------------------------------------------------
    def findLUSlength(self, strs: List[str]) -> int:

        # Sort by descending length
        strs.sort(key=len, reverse=True)

        def isSubseq(s, t):
            i = 0
            for ch in t:
                if i < len(s) and s[i] == ch:
                    i += 1
            return i == len(s)

        n = len(strs)

        for i in range(n):

            valid = True

            for j in range(n):

                if i == j:
                    continue

                # Only need to check longer or equal strings
                if len(strs[j]) < len(strs[i]):
                    break

                if isSubseq(strs[i], strs[j]):
                    valid = False
                    break

            if valid:
                return len(strs[i])

        return -1

    # -------------------------------------------------------
    # Method 2: Frequency Optimization
    # -------------------------------------------------------
    def findLUSlengthFreq(self, strs: List[str]) -> int:

        from collections import Counter

        freq = Counter(strs)

        # Unique strings only
        unique = [s for s in strs if freq[s] == 1]

        unique.sort(key=len, reverse=True)

        def isSubseq(s, t):
            i = 0
            for ch in t:
                if i < len(s) and s[i] == ch:
                    i += 1
            return i == len(s)

        for s in unique:

            ok = True

            for t in strs:

                if len(t) < len(s):
                    continue

                if s != t and isSubseq(s, t):
                    ok = False
                    break

            if ok:
                return len(s)

        return -1

