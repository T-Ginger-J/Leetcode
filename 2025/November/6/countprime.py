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

    def countPrimesPrune(self, n: int) -> int:
        if n < 3:
            return 0
        sieve = [True] * n
        sieve[0] = sieve[1] = False
        for i in range(3, int(n**0.5) + 1, 2):
            if sieve[i]:
                sieve[i*i:n:i*2] = [False] * len(range(i*i, n, i*2))
        return sum(sieve) - sum(sieve[::2]) + 1  # adjust for even numbers


sol = Solution()
print(sol.countPrimes(10))  # 4
print(sol.countPrimes(0))   # 0
print(sol.countPrimes(1))   # 0
