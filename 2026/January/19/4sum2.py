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

    # Method 2: Sorting + Two Pointers
    def fourSumCountTwoPointers(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        AB = [a + b for a in A for b in B]
        CD = [c + d for c in C for d in D]
        AB.sort()
        CD.sort()

        i, j = 0, len(CD) - 1
        count = 0

        while i < len(AB) and j >= 0:
            s = AB[i] + CD[j]
            if s == 0:
                a_val, c_val = AB[i], CD[j]
                cnt_a = cnt_c = 0
                while i < len(AB) and AB[i] == a_val:
                    cnt_a += 1
                    i += 1
                while j >= 0 and CD[j] == c_val:
                    cnt_c += 1
                    j -= 1
                count += cnt_a * cnt_c
            elif s < 0:
                i += 1
            else:
                j -= 1

        return count


# Additional Examples (Edge Cases and Non-LeetCode Examples)

sol = Solution()

# Example 1: Simple balanced arrays
A1 = [1, 2]
B1 = [-2, -1]
C1 = [-1, 2]
D1 = [0, 2]
print(sol.fourSumCount(A1, B1, C1, D1))
# Expected output: 2

# Example 2: All zeros
A2 = [0, 0]
B2 = [0, 0]
C2 = [0, 0]
D2 = [0, 0]
print(sol.fourSumCount(A2, B2, C2, D2))
# Expected output: 16

# Example 3: No valid tuples
A3 = [1]
B3 = [1]
C3 = [1]
D3 = [1]
print(sol.fourSumCount(A3, B3, C3, D3))
# Expected output: 0
