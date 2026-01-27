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


# Alternate Python Solution: Optimized Counting (No Full Count at End)
# - Count '1's while building the string.
# - Avoids slicing at the end.

class SolutionOptimized:
    def magicalString(self, n: int) -> int:
        if n <= 0:
            return 0
        if n <= 3:
            return 1

        s = [1, 2, 2]
        i = 2
        num = 1
        ones = 1

        while len(s) < n:
            count = s[i]
            for _ in range(count):
                s.append(num)
                if num == 1 and len(s) <= n:
                    ones += 1
            num = 3 - num
            i += 1

        return ones


# Additional Examples (Edge Cases and Non-LeetCode Examples)

sol = Solution()

# Example 1: Small n
print(sol.magicalString(1))
# Expected output: 1

# Example 2: First few characters
print(sol.magicalString(6))
# Expected output: 3

# Example 3: Larger n
print(sol.magicalString(15))
# Expected output: 7
