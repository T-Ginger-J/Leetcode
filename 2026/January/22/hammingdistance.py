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
