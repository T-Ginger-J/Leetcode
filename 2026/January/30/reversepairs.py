# LeetCode 493: Reverse Pairs
# Explanation:
# Given an array, count the number of reverse pairs (i, j) such that
# i < j and nums[i] > 2 * nums[j].
#
# Method 1: Merge Sort with Counting (Optimal)
# - Similar to counting inversions.
# - During merge, count pairs across left and right halves satisfying nums[i] > 2*nums[j].
#
# Time Complexity: O(n log n)
# Space Complexity: O(n) for merge

from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge_sort(l, r):
            if l >= r:
                return 0
            m = (l + r) // 2
            count = merge_sort(l, m) + merge_sort(m + 1, r)
            j = m + 1
            for i in range(l, m + 1):
                while j <= r and nums[i] > 2 * nums[j]:
                    j += 1
                count += j - (m + 1)
            # merge step
            temp = []
            i, j = l, m + 1
            while i <= m and j <= r:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1
            while i <= m:
                temp.append(nums[i])
                i += 1
            while j <= r:
                temp.append(nums[j])
                j += 1
            nums[l:r+1] = temp
            return count
        
        return merge_sort(0, len(nums) - 1)


# Alternate Python Solution: Binary Indexed Tree (BIT)
# - Map values to ranks after sorting unique elements.
# - Count using BIT while iterating from right to left.
# - Less straightforward but also O(n log n)

# Additional Examples (Edge Cases and Non-LeetCode Examples)

sol = Solution()

# Example 1: Simple reverse pair
print(sol.reversePairs([1,3,2,3,1]))
# Expected output: 2

# Example 2: No reverse pair
print(sol.reversePairs([1,2,3,4,5]))
# Expected output: 0

# Example 3: All same elements
print(sol.reversePairs([2,2,2,2]))
# Expected output: 0
