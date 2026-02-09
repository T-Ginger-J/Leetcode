# LeetCode 526: Beautiful Arrangement
# Explanation:
# 1. We need to count the number of beautiful arrangements of numbers 1..n.
# 2. A beautiful arrangement satisfies: at position i (1-indexed), either
#    - number % i == 0 or i % number == 0
# 3. Use backtracking (DFS) to generate all valid permutations.

# Methods Used:
# - Backtracking with Visited Array
# - Pruning Invalid Choices

# Time Complexity:
# - O(n!), n <= 15, but pruning reduces search space significantly

# Space Complexity:
# - O(n) for visited array and recursion stack


class Solution:

    # -------------------------------------------------------
    # Method 1: Backtracking (Optimal)
    # -------------------------------------------------------
    def countArrangement(self, n: int) -> int:

        def backtrack(pos, used):
            if pos > n:
                return 1

            count = 0

            for num in range(1, n + 1):

                if not used[num] and (num % pos == 0 or pos % num == 0):

                    used[num] = True
                    count += backtrack(pos + 1, used)
                    used[num] = False

            return count

        used = [False] * (n + 1)
        return backtrack(1, used)


