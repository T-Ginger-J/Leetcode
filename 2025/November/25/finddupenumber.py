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

    def findDuplicateBinSearch(self, nums):
        left, right = 1, len(nums)-1
        while left < right:
            mid = (left + right)//2
            count = sum(num <= mid for num in nums)
            if count > mid:
                right = mid
            else:
                left = mid + 1
        return left
    
    def findDuplicateOneLine(self, nums):
        seen = set()
        return next(x for x in nums if x in seen or seen.add(x))

print(Solution().findDuplicate([1,3,4,2,2]))  # Output: 2
print(Solution().findDuplicate([3,1,3,4,2]))  # Output: 3
print(Solution().findDuplicate([1,1]))        # Output: 1
