# LeetCode 135: Candy
# Explanation:
# 1. Each child must have at least one candy.
# 2. Children with a higher rating than their neighbors must get more candies.
# 3. Two-pass greedy approach:
#    - Left to right: If rating[i] > rating[i-1], candies[i] = candies[i-1] + 1
#    - Right to left: If rating[i] > rating[i+1], candies[i] = max(candies[i], candies[i+1] + 1)
# 4. Return the sum of candies.
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def candy(self, ratings: list[int]) -> int:
        n = len(ratings)
        candies = [1] * n

        # Left to right
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Right to left
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)
    
    def candyHillClimb(self, ratings: list[int]) -> int:
        up = down = peak = 0
        candies = 1
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                up += 1
                peak = up
                down = 0
                candies += 1 + up
            elif ratings[i] == ratings[i - 1]:
                up = down = peak = 0
                candies += 1
            else:
                up = 0
                down += 1
                candies += 1 + down - (1 if peak >= down else 0)
        return candies
