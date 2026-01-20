# LeetCode 453: Minimum Moves to Equal Array Elements
# Explanation:
# Given an integer array nums, in one move you can increment n - 1 elements by 1.
# Find the minimum number of moves to make all elements equal.
#
# Key Insight:
# - Incrementing n-1 elements by 1 is equivalent to decrementing 1 element by 1.
# - Therefore, the goal becomes reducing all elements down to the minimum value.
#
# Method 1: Mathematical Reduction (Optimal)
# - Let min_val be the minimum element in nums.
# - Each element nums[i] needs (nums[i] - min_val) decrements.
# - Total moves = sum(nums) - min_val * n
#
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Method 2: Sorting-Based (Alternative, clearer intuition)
# - Sort the array.
# - Accumulate differences between elements and the smallest value.
#
# Time Complexity: O(n log n)
# Space Complexity: O(1) or O(n) depending on sort implementation

from typing import List

class Solution:
    # Method 1: Math (Optimal)
    def minMoves(self, nums: List[int]) -> int:
        min_val = min(nums)
        return sum(nums) - min_val * len(nums)

    # Method 2: Sorting-Based
    def minMovesSort(self, nums: List[int]) -> int:
        nums.sort()
        moves = 0
        base = nums[0]
        for num in nums:
            moves += num - base
        return moves


# Additional Examples (Edge Cases and Non-LeetCode Examples)

sol = Solution()

# Example 1: Already equal
print(sol.minMoves([5,5,5]))
# Expected output: 0

# Example 2: Simple case
print(sol.minMoves([1,2,3]))
# Expected output: 3
# Explanation: Reduce 3->1 (2 moves), 2->1 (1 move)

# Example 3: Negative numbers
print(sol.minMoves([-1,0,2]))
# Expected output: 4
# Explanation: Reduce 2->-1 (3 moves), 0->-1 (1 move)
