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
