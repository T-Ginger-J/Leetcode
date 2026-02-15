class Solution:

    # -------------------------------------------------------
    # Method 1: Simple string checks
    # -------------------------------------------------------
    def checkRecord(self, s: str) -> bool:
        return s.count('A') < 2 and 'LLL' not in s

