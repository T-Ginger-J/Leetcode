class Solution:
    # Method 1: Optimal Prefix Counting
    def findKthNumber(self, n: int, k: int) -> int:
        def count_steps(prefix: int, next_prefix: int) -> int:
            steps = 0
            while prefix <= n:
                steps += min(n + 1, next_prefix) - prefix
                prefix *= 10
                next_prefix *= 10
            return steps

        curr = 1
        k -= 1  # We start at 1

        while k > 0:
            steps = count_steps(curr, curr + 1)
            if steps <= k:
                curr += 1
                k -= steps
            else:
                curr *= 10
                k -= 1

        return curr

