# LeetCode 81: Search in Rotated Sorted Array II
# Explanation:
# 1. Use modified binary search.
# 2. Skip duplicates at boundaries.
# 3. Decide which half is sorted, then check if target lies in that half.
# Time Complexity: O(log n) average, O(n) worst case (all duplicates).
# Space Complexity: O(1)

class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return True
            if nums[l] == nums[mid] == nums[r]:
                l, r = l + 1, r - 1
            elif nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False

    searchBuiltIn=lambda s,A,t:t in A

# Example usage:
# sol = Solution()
# print(sol.search([2,5,6,0,0,1,2], 0))  # True
# print(sol.search([2,5,6,0,0,1,2], 3))  # False
