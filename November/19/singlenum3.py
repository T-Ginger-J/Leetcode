# LeetCode 260 — Single Number III
# Explanation:
# 1. XOR all numbers to get xor = a ^ b, where a and b are the unique numbers.
# 2. Find a bit that is set in xor (rightmost set bit).
# 3. Partition numbers into two groups based on this bit.
# 4. XOR each group to find the two unique numbers.
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        xor = 0
        for num in nums:
            xor ^= num
        
        # Get rightmost set bit
        diff_bit = xor & -xor
        
        a = b = 0
        for num in nums:
            if num & diff_bit:
                a ^= num
            else:
                b ^= num
        return [a, b]
