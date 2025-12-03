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

