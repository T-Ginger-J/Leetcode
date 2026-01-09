# LeetCode 412: Fizz Buzz
# Explanation:
# 1. Iterate from 1 to n
# 2. Check multiples of 3 and 5
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        res = []
        for i in range(1, n+1):
            if i % 15 == 0:
                res.append("FizzBuzz")
            elif i % 3 == 0:
                res.append("Fizz")
            elif i % 5 == 0:
                res.append("Buzz")
            else:
                res.append(str(i))
        return res
