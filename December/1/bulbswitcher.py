# LeetCode 319: Bulb Switcher
# Explanation:
# Bulb i is toggled once for every divisor it has.
# A bulb ends ON only if it is toggled an odd number of times.
# Only perfect squares have an odd number of divisors.
#
# Therefore:
#   The answer is simply: how many perfect squares ≤ n?
#   => floor(sqrt(n))
#
# Time Complexity: O(1)
# Space Complexity: O(1)

class Solution:
    def bulbSwitch(self, n: int) -> int:
        from math import isqrt
        return isqrt(n)

print(Solution().bulbSwitch(3))    # 1   (only bulb 1 is on)
print(Solution().bulbSwitch(10))   # 3   (bulbs 1,4,9)
print(Solution().bulbSwitch(9999)) # 99
