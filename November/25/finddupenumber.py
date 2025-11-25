# LeetCode 287: Find the Duplicate Number
# Explanation:
# 1. We are given an array nums of n+1 integers where each integer is in [1, n].
# 2. The array contains **exactly one duplicate**, but it can appear multiple times.
# 3. Use **Floyd's Tortoise and Hare** (cycle detection):
#    - Treat nums as a linked list where value points to the next index.
#    - Detect cycle using slow and fast pointers.
#    - The entry point of the cycle is the duplicate number.
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def findDuplicate(self, nums):
        # Phase 1: Detect intersection point
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        # Phase 2: Find entrance to cycle
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
