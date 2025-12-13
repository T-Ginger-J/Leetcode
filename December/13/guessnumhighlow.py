# LeetCode 374: Guess Number Higher or Lower
# Explanation:
# 1. Standard binary search using the guess API.
# Time Complexity: O(log n)
# Space Complexity: O(1)

# The guess API is pre-defined (for testing)
def guess(num: int) -> int:
    target = 6  # Example target
    if num == target:
        return 0
    elif num > target:
        return -1
    else:
        return 1

class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n
        while low <= high:
            mid = (low + high) // 2
            g = guess(mid)
            if g == 0:
                return mid
            elif g < 0:
                high = mid - 1
            else:
                low = mid + 1

