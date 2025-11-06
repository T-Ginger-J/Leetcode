# LeetCode 204: Count Primes
# Explanation:
# 1. Use Sieve of Eratosthenes to mark non-primes.
# 2. Initialize an array is_prime where True means prime.
# 3. Starting from 2, mark all multiples as False.
# 4. Count remaining True values.
# Time Complexity: O(n log log n)
# Space Complexity: O(n)

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False
        p = 2
        while p * p < n:
            if is_prime[p]:
                for i in range(p * p, n, p):
                    is_prime[i] = False
            p += 1
        return sum(is_prime)
