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

    # -------------------------------------------------------
    # Method 2: Modify nums in-place to mark visited
    # -------------------------------------------------------
    def arrayNestingInPlace(self, nums: List[int]) -> int:
        max_len = 0
        for i in range(len(nums)):
            count = 0
            start = i
            while nums[start] != -1:
                temp = start
                start = nums[start]
                nums[temp] = -1
                count += 1
            max_len = max(max_len, count)
        return max_len


# -------------------------------------------------------
# Examples & Edge Cases
# -------------------------------------------------------

sol = Solution()

# Example 1
nums1 = [5,4,0,3,1,6,2]
print(sol.arrayNesting(nums1[:]))           # 4 (sequence: 0->5->6->2->0)
print(sol.arrayNestingInPlace(nums1[:]))    # 4

# Example 2: single element
nums2 = [0]
print(sol.arrayNesting(nums2[:]))           # 1

# Example 3: two elements
nums3 = [1,0]
print(sol.arrayNesting(nums3[:]))           # 2

# Example 4: sequential cycle
nums4 = [0,1,2,3,4]
print(sol.arrayNesting(nums4[:]))           # 1

# Example 5: large cycle
nums5 = [1,2,3,4,0]
print(sol.arrayNesting(nums5[:]))           # 5
