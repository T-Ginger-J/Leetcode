# LeetCode 393: UTF-8 Validation
# Explanation:
# 1. Use bit masks to check byte patterns
# 2. Track number of continuation bytes needed
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def validUtf8(self, data: list[int]) -> bool:
        remaining = 0
        for byte in data:
            if remaining == 0:
                if (byte >> 5) == 0b110:
                    remaining = 1
                elif (byte >> 4) == 0b1110:
                    remaining = 2
                elif (byte >> 3) == 0b11110:
                    remaining = 3
                elif (byte >> 7) != 0:
                    return False
            else:
                if (byte >> 6) != 0b10:
                    return False
                remaining -= 1
        return remaining == 0

print(Solution().validUtf8([197,130,1]))       # Output: True ([110xxxxx 10xxxxxx 1])
print(Solution().validUtf8([235,140,4]))       # Output: False
print(Solution().validUtf8([0]))               # Output: True
