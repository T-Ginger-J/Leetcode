# LeetCode 551: Student Attendance Record I
# Explanation:
# 1. Given a string of 'A', 'L', 'P', determine if a student is eligible for an attendance award.
# 2. Conditions:
#    - Fewer than 2 'A's total.
#    - No occurrence of 3 or more consecutive 'L's.
# 3. Approach:
#    - Count total 'A's in the string.
#    - Check if substring 'LLL' exists in s.
# 4. Time Complexity: O(n), n = length of string
# 5. Space Complexity: O(1)

class Solution:

    # -------------------------------------------------------
    # Method 1: Simple string checks
    # -------------------------------------------------------
    def checkRecord(self, s: str) -> bool:
        return s.count('A') < 2 and 'LLL' not in s

