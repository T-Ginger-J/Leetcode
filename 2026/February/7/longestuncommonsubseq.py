class Solution:

    # -------------------------------------------------------
    # Method 1: Direct Observation (Optimal)
    # -------------------------------------------------------
    def findLUSlength(self, a: str, b: str) -> int:

        if a == b:
            return -1

        return max(len(a), len(b))

