# LeetCode 461: Hamming Distance
# Explanation:
# The Hamming distance between two integers is the number of positions
# at which the corresponding bits are different.
#
# Method 1: XOR + Bit Counting (Optimal)
# - XOR x and y → differing bits become 1
# - Count number of 1s in the result
#
# Time Complexity: O(1) (bounded by number of bits, max 32)
# Space Complexity: O(1)

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count("1")


# Additional Examples (Edge Cases and Non-LeetCode Examples)

sol = Solution()

# Example 1: Same numbers
print(sol.hammingDistance(5, 5))
# Expected output: 0

# Example 2: Completely different bits
print(sol.hammingDistance(0, 15))
# Expected output: 4

# Example 3: One-bit difference
print(sol.hammingDistance(1, 3))
# Expected output: 1
