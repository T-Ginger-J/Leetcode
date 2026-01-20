# LeetCode 454: 4Sum II
# Explanation:
# Given four integer arrays A, B, C, and D, compute how many tuples (i, j, k, l)
# such that:
#   A[i] + B[j] + C[k] + D[l] == 0
#
# Method 1: Hash Map for Pair Sums (Optimal)
# - Compute all possible sums of A[i] + B[j] and store their frequencies in a hashmap.
# - For each possible sum of C[k] + D[l], check if its negation exists in the hashmap.
# - Accumulate counts accordingly.
#
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
#
# Method 2: Sorting + Two Pointers (Alternative, same asymptotic but different tradeoffs)
# - Compute all pair sums of A+B and C+D.
# - Sort both lists.
# - Use two pointers to count complementary pairs.
#
# Time Complexity: O(n^2 log n)
# Space Complexity: O(n^2)

from typing import List
from collections import Counter

class Solution:
    # Method 1: Hash Map (Optimal)
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        ab_sum = Counter()
        for a in A:
            for b in B:
                ab_sum[a + b] += 1

        count = 0
        for c in C:
            for d in D:
                count += ab_sum.get(-(c + d), 0)

        return count
