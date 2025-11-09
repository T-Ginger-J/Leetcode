# LeetCode 213: House Robber II
# Explanation:
# 1. Same as House Robber I, but circular — can't rob both first and last houses.
# 2. Compute max from two scenarios:
#    - Rob houses [0 .. n-2]
#    - Rob houses [1 .. n-1]
# 3. Return max of the two.
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_line(houses):
            prev, curr = 0, 0
            for n in houses:
                prev, curr = curr, max(curr, prev + n)
            return curr

        return max(rob_line(nums[:-1]), rob_line(nums[1:]))

