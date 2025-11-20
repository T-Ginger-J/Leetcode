# LeetCode 264 — Ugly Number II
# Explanation:
# 1. Use dynamic programming with 3 pointers for multiples of 2, 3, and 5.
# 2. Keep track of next multiples and update pointers when used.
# 3. Generate ugly numbers until n-th.
# Time Complexity: O(n)
# Space Complexity: O(n)

import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1] * n
        i2 = i3 = i5 = 0
        next2, next3, next5 = 2, 3, 5

        for i in range(1, n):
            next_ugly = min(next2, next3, next5)
            ugly[i] = next_ugly

            if next_ugly == next2:
                i2 += 1
                next2 = ugly[i2] * 2
            if next_ugly == next3:
                i3 += 1
                next3 = ugly[i3] * 3
            if next_ugly == next5:
                i5 += 1
                next5 = ugly[i5] * 5
        return ugly[-1]
    
    def nthUglyNumberHeap(self, n: int) -> int:
        seen = {1}
        heap = [1]
        for _ in range(n-1):
            x = heapq.heappop(heap)
            for factor in [2,3,5]:
                if x*factor not in seen:
                    seen.add(x*factor)
                    heapq.heappush(heap, x*factor)
        return heapq.heappop(heap)


# Example usage:
# sol = Solution()
# print(sol.nthUglyNumber(10))  # 12
# print(sol.nthUglyNumber(1))   # 1
