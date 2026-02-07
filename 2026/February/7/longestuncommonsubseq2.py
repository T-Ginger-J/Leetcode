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
