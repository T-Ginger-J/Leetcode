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

