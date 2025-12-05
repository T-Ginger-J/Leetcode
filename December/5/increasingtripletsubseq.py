# LeetCode 334: Increasing Triplet Subsequence
# Explanation:
# We want: i < j < k such that nums[i] < nums[j] < nums[k]
#
# Greedy Idea:
# Keep track of the smallest and second smallest numbers seen so far:
#   - first  = smallest so far
#   - second = smallest > first
#
# If we ever find a number > second → we found a triplet.
#
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def increasingTriplet(self, nums):
        first = second = float('inf')

        for x in nums:
            if x <= first:
                first = x
            elif x <= second:
                second = x
            else:
                # x > second → triplet found
                return True

        return False

# Example 1
nums = [1, 2, 3, 4, 5]
# Output: True → (1,2,3)
print(Solution().increasingTriplet(nums))

# Example 2
nums = [5, 4, 3, 2, 1]
# Output: False
print(Solution().increasingTriplet(nums))

# Example 3
nums = [2,1,5,0,4,6]
# Output: True → (0,4,6)
print(Solution().increasingTriplet(nums))
