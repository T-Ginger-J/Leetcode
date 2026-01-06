# LeetCode 137: Single Number II
# Explanation:
# 1. Every element appears three times except one.
# 2. Use bit manipulation:
#    - Track bits appearing once (`ones`) and twice (`twos`).
#    - For each number:
#        ones = (ones ^ num) & ~twos
#        twos = (twos ^ num) & ~ones
#    - Ensures bits seen thrice are cleared from both.
# 3. Result stored in `ones`.
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ones, twos = 0, 0
        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones
        return ones

print(Solution().singleNumber([2,2,3,2]))
# Output: 3

print(Solution().singleNumber([0,1,0,1,0,1,99]))
# Output: 99

print(Solution().singleNumber([-2,-2,1,1,4,1,4,4,-4,-2]))
# Output: -4
