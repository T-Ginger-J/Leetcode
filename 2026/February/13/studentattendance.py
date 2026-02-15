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

    # -------------------------------------------------------
    # Method 2: Iterative check (without built-in count / substring)
    # -------------------------------------------------------
    def checkRecordIterative(self, s: str) -> bool:
        absences = 0
        consecutive_l = 0
        for c in s:
            if c == 'A':
                absences += 1
                if absences >= 2:
                    return False
                consecutive_l = 0
            elif c == 'L':
                consecutive_l += 1
                if consecutive_l >= 3:
                    return False
            else:
                consecutive_l = 0
        return True


# -------------------------------------------------------
# Examples & Edge Cases
# -------------------------------------------------------

# Example 1
s1 = "PPALLP"
print(Solution().checkRecord(s1))           # True
print(Solution().checkRecordIterative(s1))  # True

# Example 2
s2 = "PPALLL"
print(Solution().checkRecord(s2))           # False
print(Solution().checkRecordIterative(s2))  # False

# Example 3: Exactly one absence, no late streak
s3 = "PAPPP"
print(Solution().checkRecord(s3))           # True

# Example 4: Two absences
s4 = "PAAPP"
print(Solution().checkRecord(s4))           # False

# Example 5: Three consecutive lates
s5 = "PLPLLLP"
print(Solution().checkRecord(s5))           # False

# Example 6: Empty string
s6 = ""
print(Solution().checkRecord(s6))           # True
