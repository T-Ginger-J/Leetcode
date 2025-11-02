# LeetCode 191: Number of 1 Bits
# Explanation:
# 1. Count how many bits are set to 1 in the binary representation of n.
# 2. Keep checking the last bit using n & 1, then right shift n.
# 3. Continue until n becomes 0.
# Time Complexity: O(1)  (since there are always 32 bits)
# Space Complexity: O(1)

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count


    def hammingWeightOptimized(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count


    def hammingWeightOneLine(self, n: int) -> int: return bin(n).count('1')

sol = Solution()
print(sol.hammingWeight(0b00000000000000000000000000001011))  # 3
print(sol.hammingWeight(0b00000000000000000000000010000000))  # 1
print(sol.hammingWeight(0b11111111111111111111111111111101))  # 31


