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

