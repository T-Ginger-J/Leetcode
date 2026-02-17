# LeetCode 565: Array Nesting
# Explanation:
# 1. Given an array nums where 0 ≤ nums[i] < n and all elements are unique, define S[i] = {nums[i], nums[nums[i]], ...} until a duplicate is found.
# 2. Task: Find the size of the largest set S[i].
# 3. Approach:
#    - For each unvisited index, traverse the sequence using nums[i] until a cycle is detected.
#    - Keep track of visited indices to avoid recomputation.
#    - Update maximum length encountered.
# 4. Time Complexity: O(n), each index visited at most once
# 5. Space Complexity: O(n) for visited set (can also modify nums in-place)

from typing import List

class Solution:

    # -------------------------------------------------------
    # Method 1: Using visited set
    # -------------------------------------------------------
    def arrayNesting(self, nums: List[int]) -> int:
        visited = set()
        max_len = 0
        for i in range(len(nums)):
            if i not in visited:
                start = i
                count = 0
                while start not in visited:
                    visited.add(start)
                    start = nums[start]
                    count += 1
                max_len = max(max_len, count)
        return max_len

