# LeetCode 60: Permutation Sequence
# Explanation:
# 1. The number of permutations for n elements is n!.
# 2. Fix the first digit by determining how many permutations are in each block of size (n-1)!.
# 3. Use k to find which block to choose and remove that element.
# 4. Repeat for the remaining numbers.
# Time Complexity: O(n^2) (because list removals are O(n) and we do it n times)
# Space Complexity: O(n)

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        import math
        nums = [str(i) for i in range(1, n+1)]
        k -= 1
        result = []
        for i in range(n, 0, -1):
            f = math.factorial(i-1)
            index = k // f
            result.append(nums.pop(index))
            k %= f
        return ''.join(result)

# Example usage:
# sol = Solution()
# print(sol.getPermutation(3, 3))  # "213"
# print(sol.getPermutation(4, 9))  # "2314"
