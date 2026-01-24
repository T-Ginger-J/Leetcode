# LeetCode 470: Implement Rand10() Using Rand7()
# Explanation:
# Given rand7() that returns a uniform random integer from 1 to 7,
# implement rand10() that returns a uniform random integer from 1 to 10.
#
# Method 1: Rejection Sampling (Optimal)
# - Generate a uniform number in [1,49] using:
#     num = (rand7() - 1) * 7 + rand7()
# - If num <= 40, map it to [1,10] using (num - 1) % 10 + 1
# - Otherwise, reject and retry.
#
# Why it works:
# - 49 outcomes equally likely.
# - First 40 map evenly to 1..10 (each appears 4 times).
#
# Expected Time Complexity: O(1)
# Space Complexity: O(1)

import random

def rand7():
    return random.randint(1, 7)

class Solution:
    def rand10(self) -> int:
        while True:
            num = (rand7() - 1) * 7 + rand7()  # 1..49
            if num <= 40:
                return (num - 1) % 10 + 1


# Alternate Python Solution: Multi-Stage Rejection (Uses leftover entropy)
# - Reduce wasted samples by reusing rejected values.
# - Improves expected number of rand7() calls.

class SolutionOptimized:
    def rand10(self) -> int:
        while True:
            a = rand7()
            b = rand7()
            idx = (a - 1) * 7 + b  # 1..49
            if idx <= 40:
                return (idx - 1) % 10 + 1

            idx = idx - 40  # 1..9
            b = rand7()
            idx = (idx - 1) * 7 + b  # 1..63
            if idx <= 60:
                return (idx - 1) % 10 + 1

            idx = idx - 60  # 1..3
            b = rand7()
            idx = (idx - 1) * 7 + b  # 1..21
            if idx <= 20:
                return (idx - 1) % 10 + 1
