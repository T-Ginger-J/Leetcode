# LeetCode 414: Third Maximum Number
# Explanation:
# 1. Track first, second, third maximum distinct numbers
# 2. Skip duplicates
# 3. Return third if exists, else first
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        first = second = third = None
        for num in nums:
            if num in (first, second, third):
                continue
            if first is None or num > first:
                first, second, third = num, first, second
            elif second is None or num > second:
                second, third = num, second
            elif third is None or num > third:
                third = num
        return third if third is not None else first

print(Solution().thirdMax([3,2,1]))     # Output: 1
print(Solution().thirdMax([1,2]))       # Output: 2
print(Solution().thirdMax([2,2,3,1]))   # Output: 1
