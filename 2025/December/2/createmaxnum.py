# LeetCode 321: Create Maximum Number
# Explanation:
# We must create the largest possible number of length k by choosing digits
# from nums1 and nums2 while keeping internal order of each array.
#
# Strategy:
# 1. For every possible split (i digits from nums1, k-i from nums2):
#       - Extract max subsequence from nums1 of size i
#       - Extract max subsequence from nums2 of size k-i
#       - Merge them greedily into the largest possible sequence
# 2. Keep the best sequence seen.
#
# Key subroutines:
#   - max_subsequence(nums, k): monotonic stack to get max length-k subsequence
#   - merge(a, b): lexicographically merge two lists
#
# Time Complexity: O(k * (n1+n2)) for all splits
# Space Complexity: O(k)

class Solution:
    def maxNumber(self, nums1, nums2, k):
        
        # pick max subsequence of length k
        def max_subsequence(nums, k):
            drop = len(nums) - k
            stack = []
            for n in nums:
                while drop and stack and stack[-1] < n:
                    stack.pop()
                    drop -= 1
                stack.append(n)
            return stack[:k]
        
        # merge two sequences into the largest possible lexicographically
        def merge(a, b):
            res = []
            while a or b:
                if a > b:
                    res.append(a.pop(0))
                else:
                    res.append(b.pop(0))
            return res

        best = []
        n1, n2 = len(nums1), len(nums2)
        
        for i in range(max(0, k - n2), min(k, n1) + 1):
            seq1 = max_subsequence(nums1, i)
            seq2 = max_subsequence(nums2, k - i)
            candidate = merge(seq1.copy(), seq2.copy())
            best = max(best, candidate)
        
        return best

print(Solution().maxNumber([3,4,6,5], [9,1,2,5,8,3], 5))
# Output: [9, 8, 6, 5, 3]

print(Solution().maxNumber([6,7], [6,0,4], 5))
# Output: [6,7,6,0,4]

print(Solution().maxNumber([3,9], [8,9], 3))
# Output: [9,9,8]
