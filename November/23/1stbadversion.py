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
