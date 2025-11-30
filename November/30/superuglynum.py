# LeetCode 313: Super Ugly Number
# Explanation:
# 1. Use a min-heap to generate super ugly numbers in ascending order.
# 2. Start with 1 and multiply by each prime to generate next candidates.
# 3. Use a set to avoid duplicates.
# Time Complexity: O(n * log(n)), due to heap operations
# Space Complexity: O(n)

import heapq

class Solution:
    def nthSuperUglyNumber(self, n, primes):
        heap = [1]
        seen = {1}
        val = 1
        for _ in range(n):
            val = heapq.heappop(heap)
            for p in primes:
                new_val = val * p
                if new_val not in seen:
                    seen.add(new_val)
                    heapq.heappush(heap, new_val)
        return val

    def nthSuperUglyNumberDP(self, n, primes):
        size = len(primes)
        ugly = [1]*n
        idx = [0]*size
        next_mul = primes[:]
        for i in range(1,n):
            next_ugly = min(next_mul)
            ugly[i] = next_ugly
            for j in range(size):
                if next_mul[j] == next_ugly:
                    idx[j] += 1
                    next_mul[j] = ugly[idx[j]] * primes[j]
        return ugly[-1]
