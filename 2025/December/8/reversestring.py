# LeetCode 344: Reverse String
# Explanation:
# 1. Use two pointers: left and right.
# 2. Swap characters until they meet.
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def reverseString(self, s):
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

    def reverseStringOneLine(self, s):
        s[:] = s[::-1]

arr = ["h","e","l","l","o"]
Solution().reverseString(arr)
print(arr)  # Output: ["o","l","l","e","h"]

