# LeetCode 179: Largest Number
# Explanation:
# 1. Convert all integers to strings for custom sorting.
# 2. Sort numbers such that concatenation (a+b) > (b+a) determines order.
# 3. Join sorted strings to form the largest number.
# 4. Edge case: If the largest number starts with '0', return '0' (e.g. [0,0]).
# Time Complexity: O(n log n) due to sorting.
# Space Complexity: O(n) for string conversions.


class Solution:
    def largestNumber(self, nums):
        from functools import cmp_to_key
        
        def compare(a, b):
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            else:
                return 0
