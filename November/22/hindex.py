# LeetCode 274: H-Index
# Explanation:
# 1. Sort citations descending.
# 2. h-index is the largest i such that citations[i] >= i+1.
#
# Time Complexity: O(n log n)
# Space Complexity: O(1)

class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort(reverse=True)
        h = 0
        for i, c in enumerate(citations):
            if c >= i + 1:
                h = i + 1
        return h

# Example usage:
# sol = Solution()
# print(sol.hIndex([3,0,6,1,5]))   # 3
# print(sol.hIndex([1,3,1]))       # 1
# print(sol.hIndex([0,0,0]))       # 0
