# LeetCode 481: Magical String
# Explanation:
# A magical string is a string consisting of only '1' and '2' where
# the counts of consecutive groups form the string itself.
#
# The string starts as: "1221121221221121122..."
#
# Goal:
# - Given n, return the number of '1's in the first n characters.
#
# Method 1: Simulation with Two Pointers (Optimal)
# - Build the magical string iteratively.
# - Use a pointer i to read counts.
# - Append either '1' or '2' based on previous value.
#
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def magicalString(self, n: int) -> int:
        if n <= 0:
            return 0
        if n <= 3:
            return 1

        s = [1, 2, 2]
        i = 2
        num = 1

        while len(s) < n:
            count = s[i]
            s.extend([num] * count)
            num = 3 - num
            i += 1

        return s[:n].count(1)


