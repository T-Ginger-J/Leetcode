# LeetCode 553: Optimal Division
# Explanation:
# 1. Given a list of numbers, divide them in a way to maximize the result.
# 2. Observation:
#    - For numbers [a1, a2, ..., an], to maximize a1 / a2 / ... / an, we should minimize the denominator.
#    - Minimizing denominator means grouping a2/.../an in parentheses: a1 / (a2 / ... / an) = a1 / (a2 * a3 * ... * an)
# 3. Approach:
#    - If length is 1: return str(nums[0])
#    - If length is 2: return "a1/a2"
#    - If length >2: return "a1/(a2/a3/.../an)"

# Time Complexity:
# - O(n), n = length of nums (building the string)
# Space Complexity:
# - O(n), string length

from typing import List

class Solution:

    # -------------------------------------------------------
    # Method 1: Direct construction
    # -------------------------------------------------------
    def optimalDivision(self, nums: List[int]) -> str:
        if not nums:
            return ""
        if len(nums) == 1:
            return str(nums[0])
        if len(nums) == 2:
            return f"{nums[0]}/{nums[1]}"
        return f"{nums[0]}/({'/'.join(map(str, nums[1:]))})"

    # -------------------------------------------------------
    # Method 2: Recursive (not needed but alternative)
    # -------------------------------------------------------
    def optimalDivisionRecursive(self, nums: List[int]) -> str:
        if len(nums) == 1:
            return str(nums[0])
        if len(nums) == 2:
            return f"{nums[0]}/{nums[1]}"
        return f"{nums[0]}/({self.optimalDivisionRecursive(nums[1:])})"
