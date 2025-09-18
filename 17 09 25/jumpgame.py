#O(n)

from functools import reduce

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        max_reach = 0
        for i, n in enumerate(nums):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + n)
        return True
    
    def canJumpOptimized(self, nums: list[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0

    # ---- Example Tests ----
sol = Solution()

print(sol.canJump([2,3,1,1,4]))  # True
# Explanation: You can jump 2 → index 2 (or 1) → ... → last index

print(sol.canJump([3,2,1,0,4]))  # False
# Explanation: You will get stuck at index 3 (value 0)

print(sol.canJump([0]))          # True
# Explanation: Already at the last index

print(sol.canJump([1,0,2]))      # False
# Can't get past index 1 (value 0)

