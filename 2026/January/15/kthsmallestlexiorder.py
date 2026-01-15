# LeetCode 440: K-th Smallest in Lexicographical Order
# Explanation:
# We are given integers n and k. Consider all numbers from 1 to n sorted
# in lexicographical (dictionary) order. The goal is to find the k-th number.
#
# Key Insight:
# - Lexicographical order can be visualized as a prefix tree (trie).
# - Each number is a node, and children are formed by appending digits 0–9.
# - Instead of generating all numbers (too slow), we count how many numbers
#   exist under a given prefix and skip entire subtrees when possible.
#
# Method 1: Prefix Counting (Optimal)
# - Start from prefix = 1.
# - At each step, count how many numbers are between:
#     prefix and prefix + 1
#   within the range [1, n].
# - If the count <= k, skip this prefix subtree.
# - Otherwise, go deeper (prefix *= 10).
#
# Time Complexity: O(log(n)^2)
# Space Complexity: O(1)
#
# If brute force were attempted:
# - Time Complexity: O(n log n)
# - Space Complexity: O(n)
# This is too slow for n up to 10^9 and is therefore not implemented.

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


# Additional Examples (Edge Cases and Non-LeetCode Examples)

# Example 1: Small n, small k
print(Solution().findKthNumber(13, 2))   # Expected: 10

# Example 2: k points to last element
print(Solution().findKthNumber(20, 20))  # Expected: 9

# Example 3: n is a power of 10 boundary
print(Solution().findKthNumber(100, 90)) # Expected: 9
