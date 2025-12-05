# LeetCode 330: Patching Array
# Explanation:
# We want to cover all numbers in the range [1, n] using:
#   - Existing sorted nums[]
#   - Additional "patch" numbers we add
#
# Key Greedy Insight:
# If we can cover [1, miss), and the next number is x:
#   - If x <= miss, we extend coverage to [1, miss + x)
#   - If x > miss, we must patch with "miss"
#       (this doubles the coverage to [1, miss + miss))
#
# Time Complexity: O(len(nums) + log n)
# Space Complexity: O(1)

class Solution:
    def minPatches(self, nums, n):
        miss = 1     # smallest number that cannot yet be formed
        patches = 0
        i = 0

        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                # patch with 'miss'
                miss += miss
                patches += 1

        return patches

# Example 1
nums = [1, 3]
n = 6
# Output: 1 (patch with 2)
print(Solution().minPatches(nums, n))  # 1

# Example 2
nums = [1, 5, 10]
n = 20
# Output: 2 (patch with 2, 4)
print(Solution().minPatches(nums, n))  # 2

# Example 3
nums = [1, 2, 2]
n = 5
# Output: 0 (already covers everything)
print(Solution().minPatches(nums, n))  # 0
p