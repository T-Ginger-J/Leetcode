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

print(Solution().fizzBuzz(15))
# Output:
# ['1','2','Fizz','4','Buzz','Fizz','7','8','Fizz','Buzz',
#  '11','Fizz','13','14','FizzBuzz']
