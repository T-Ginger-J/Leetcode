# LeetCode 134: Gas Station
# Explanation:
# 1. You have two arrays: gas[i] (gas available) and cost[i] (gas needed to travel to next station).
# 2. If total gas < total cost, it’s impossible → return -1.
# 3. Use a greedy approach:
#    - Traverse stations, maintaining current gas balance.
#    - If balance drops below 0, start from next station.
# 4. The final start index (if total gas ≥ total cost) is the solution.
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        total, curr, start = 0, 0, 0
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total += diff
            curr += diff
            if curr < 0:
                curr = 0
                start = i + 1
        return start if total >= 0 else -1
