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
