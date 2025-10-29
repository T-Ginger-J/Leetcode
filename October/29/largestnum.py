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
        
        nums = list(map(str, nums))
        nums.sort(key=cmp_to_key(compare))
        result = ''.join(nums)
        return '0' if result[0] == '0' else result

    def largestNumberLambda(self, nums):
        nums = sorted(map(str, nums), key=lambda x: x*10, reverse=True)
        res = ''.join(nums)
        return '0' if res[0] == '0' else res

    largestNumberOneLine = lambda self, nums: '0' if (s:=''.join(sorted(map(str, nums), key=lambda x:x*10, reverse=True)))[0]=='0' else s
