# LeetCode 275: H-Index II
# Explanation:
# 1. We need the largest h such that citations[n - h] >= h.
# 2. Use binary search on h from 0..n.
# 
# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution:
    def hIndex(self, citations: list[int]) -> int:
        n = len(citations)
        left, right = 0, n

        while left < right:
            mid = (left + right + 1) // 2  # proposed h
            if citations[n - mid] >= mid:
                left = mid
            else:
                right = mid - 1

        return left
    
    def hIndexOneLine(self, c: list[int]) -> int:
        return max((len(c)-i for i,x in enumerate(c) if x>=len(c)-i), default=0)


# Example usage:
# sol = Solution()
# print(sol.hIndex([0,1,3,5,6]))  # 3
# print(sol.hIndex([1,2,100]))    # 2
# print(sol.hIndex([0]))          # 0
