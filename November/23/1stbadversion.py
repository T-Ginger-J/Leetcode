# LeetCode 278: First Bad Version
# Explanation:
# 1. We are given a function isBadVersion(version) which returns True if the version is bad.
# 2. Goal: Find the first bad version.
# 3. Use binary search since versions are sequential.
# 4. At each step:
#    - Check mid version.
#    - If mid is bad, first bad is <= mid, search left half.
#    - If mid is good, first bad is > mid, search right half.
# Time Complexity: O(log n)
# Space Complexity: O(1)

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left

# Suppose version 4 is the first bad version
bad_version = 4

def isBadVersion(version):
    return version >= bad_version

print(Solution().firstBadVersion(5))  # Output: 4
print(Solution().firstBadVersion(10)) # Output: 4
