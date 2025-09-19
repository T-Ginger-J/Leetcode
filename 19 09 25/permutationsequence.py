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
    
    def getPermutationOptimized(self, n: int, k: int) -> str:
        fact = [1]*n
        for i in range(1, n):
            fact[i] = fact[i-1]*i
        nums = [str(i) for i in range(1, n+1)]
        k -= 1
        res = []
        for i in range(n-1, -1, -1):
            idx = k // fact[i]
            res.append(nums.pop(idx))
            k %= fact[i]
        return ''.join(res)
    
    getPermutationOneLine=lambda s,n,k:(lambda f,n,k,r:''.join(r.pop((k:=k-1)//f[i]%(n:=n)) or r for i in range(n-1,-1,-1)))(__import__('math').factorial,n,k,[str(i) for i in range(1,n+1)])


# Example usage:
# sol = Solution()
# print(sol.getPermutation(3, 3))  # "213"
# print(sol.getPermutation(4, 9))  # "2314"
