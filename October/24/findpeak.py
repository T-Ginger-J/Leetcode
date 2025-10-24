# LeetCode 162: Find Peak Element
# Explanation:
# 1. A peak element is greater than its neighbors.
# 2. Use binary search to find a peak in O(log n) time.
# 3. Compare nums[mid] with nums[mid+1]:
#    - If nums[mid] > nums[mid+1], then a peak lies on the left (including mid).
#    - Else, a peak lies on the right.
# 4. Continue until left == right; that index is a peak.
# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution:
    def findPeakElement(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left

    def findPeakElement(self, A): return self.findPeakElement(A[:len(A)//2+1]) if len(A)>1 and A[len(A)//2]<A[len(A)//2+1] else (len(A)//2 if len(A)<=1 or A[len(A)//2]>=A[len(A)//2-1] else self.findPeakElement(A[:len(A)//2]))

print(Solution().findPeakElement([1,2,3,1]))
# Output: 2  (nums[2] = 3 is a peak)

print(Solution().findPeakElement([1,2,1,3,5,6,4]))
# Output: 5  (nums[5] = 6 is a peak)

print(Solution().findPeakElement([3,2,1]))
# Output: 0  (nums[0] = 3 is a peak)
