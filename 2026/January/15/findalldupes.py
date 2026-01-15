# LeetCode 442: Find All Duplicates in an Array
# Explanation:
# Given an array nums of n integers where 1 ≤ nums[i] ≤ n, some elements appear twice.
# Goal: return all elements that appear twice without using extra space.
#
# Method 1: In-Place Negative Marking (Optimal)
# - For each number nums[i], map it to index abs(nums[i]) - 1.
# - Negate the value at that index to mark it as seen.
# - If the value is already negative, the number is a duplicate.
#
# Time Complexity: O(n)
# Space Complexity: O(1) (ignoring output list)

from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] < 0:
                res.append(abs(nums[i]))
            else:
                nums[index] = -nums[index]
        return res

# Additional Examples (Edge Cases and Non-LeetCode Examples)

sol = Solution()

# Example 1: Multiple duplicates
print(sol.findDuplicates([4,3,2,7,8,2,3,1]))  
# Expected output: [2, 3]

# Example 2: Single duplicate
print(sol.findDuplicates([1,1,2]))  
# Expected output: [1]

# Example 3: No duplicates
print(sol.findDuplicates([1,2,3,4,5]))  
# Expected output: []
